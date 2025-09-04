"""
Unit tests for thermal conductance and geometry calculations.
"""

import pytest
import numpy as np
from cryocalc.thermal import (
    ThermalCalculator,
    RodGeometry,
    TubeGeometry,
    BarGeometry,
    CustomGeometry,
    GeometryType,
    create_rod,
    create_wire,
    create_tube,
    create_bar,
    create_custom
)
from cryocalc import MaterialCalculator


class TestGeometries:
    """Test geometry classes and calculations."""
    
    def test_rod_geometry(self):
        """Test rod geometry calculations."""
        rod = RodGeometry(diameter=0.01, length=0.1)  # 10mm diameter, 100mm length
        
        assert rod.geometry_type == GeometryType.ROD
        assert abs(rod.cross_sectional_area() - np.pi * (0.005)**2) < 1e-10
        assert "rod" in rod.description().lower()
        assert "10.0mm" in rod.description()
    
    def test_wire_geometry(self):
        """Test wire geometry (small diameter rod)."""
        wire = RodGeometry(diameter=0.0005, length=0.1)  # 0.5mm diameter
        
        assert wire.geometry_type == GeometryType.WIRE
        assert abs(wire.cross_sectional_area() - np.pi * (0.00025)**2) < 1e-12
        assert "wire" in wire.description().lower()
    
    def test_tube_geometry(self):
        """Test tube geometry calculations."""
        tube = TubeGeometry(outer_diameter=0.02, wall_thickness=0.002, length=0.1)
        
        assert tube.geometry_type == GeometryType.TUBE
        outer_area = np.pi * (0.01)**2
        inner_area = np.pi * (0.008)**2
        expected_area = outer_area - inner_area
        assert abs(tube.cross_sectional_area() - expected_area) < 1e-10
        assert "tube" in tube.description().lower()
    
    def test_tube_invalid_wall_thickness(self):
        """Test tube with invalid wall thickness."""
        with pytest.raises(ValueError):
            TubeGeometry(outer_diameter=0.01, wall_thickness=0.006, length=0.1)
    
    def test_bar_geometry(self):
        """Test bar geometry calculations."""
        bar = BarGeometry(width=0.01, thickness=0.005, length=0.1)
        
        assert bar.geometry_type == GeometryType.BAR
        assert abs(bar.cross_sectional_area() - 0.01 * 0.005) < 1e-10
        assert "bar" in bar.description().lower()
    
    def test_custom_geometry(self):
        """Test custom geometry."""
        custom = CustomGeometry(area=1e-6, length=0.1, description_text="test shape")
        
        assert custom.geometry_type == GeometryType.CUSTOM
        assert custom.cross_sectional_area() == 1e-6
        assert "test shape" in custom.description()


class TestGeometryHelpers:
    """Test geometry creation helper functions."""
    
    def test_create_rod(self):
        """Test create_rod helper."""
        rod = create_rod(diameter_mm=10, length_mm=100)
        assert isinstance(rod, RodGeometry)
        assert rod.diameter == 0.01
        assert rod.length == 0.1
    
    def test_create_wire(self):
        """Test create_wire helper."""
        wire = create_wire(diameter_mm=0.5, length_mm=100)
        assert isinstance(wire, RodGeometry)
        assert wire.geometry_type == GeometryType.WIRE
    
    def test_create_tube(self):
        """Test create_tube helper."""
        tube = create_tube(outer_diameter_mm=20, wall_thickness_mm=2, length_mm=100)
        assert isinstance(tube, TubeGeometry)
        assert tube.outer_diameter == 0.02
        assert tube.wall_thickness == 0.002
    
    def test_create_bar(self):
        """Test create_bar helper."""
        bar = create_bar(width_mm=10, thickness_mm=5, length_mm=100)
        assert isinstance(bar, BarGeometry)
        assert bar.width == 0.01
        assert bar.thickness == 0.005
    
    def test_create_custom(self):
        """Test create_custom helper."""
        custom = create_custom(area_mm2=100, length_mm=50, description="test")
        assert isinstance(custom, CustomGeometry)
        assert custom.area == 100e-6
        assert custom.length == 0.05


class TestThermalCalculator:
    """Test thermal calculations."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calc = ThermalCalculator()
        self.rod = create_rod(diameter_mm=10, length_mm=100)
        self.material = "aluminum_6061_t6"
    
    def test_calculator_initialization(self):
        """Test calculator initialization."""
        assert isinstance(self.calc.calculator, MaterialCalculator)
        
        # Test with custom calculator
        custom_calc = MaterialCalculator()
        thermal_calc = ThermalCalculator(custom_calc)
        assert thermal_calc.calculator is custom_calc
    
    def test_thermal_conductivity_integral(self):
        """Test thermal conductivity integration."""
        integral = self.calc.calculate_thermal_conductivity_integral(
            self.material, 77.0, 300.0, num_points=50
        )
        
        assert isinstance(integral, float)
        assert integral > 0
        # Should be roughly k_avg * delta_T
        k_77 = self.calc.calculator.calculate_thermal_conductivity(self.material, 77.0)
        k_300 = self.calc.calculator.calculate_thermal_conductivity(self.material, 300.0)
        k_avg_approx = (k_77 + k_300) / 2
        expected_approx = k_avg_approx * (300.0 - 77.0)
        assert abs(integral - expected_approx) / expected_approx < 0.5  # Within 50%
    
    def test_thermal_conductivity_integral_invalid_range(self):
        """Test integral with invalid temperature range."""
        with pytest.raises(ValueError):
            self.calc.calculate_thermal_conductivity_integral(
                self.material, 300.0, 77.0  # reversed range
            )
    
    def test_thermal_conductivity_integral_out_of_bounds(self):
        """Test integral with out-of-bounds temperatures."""
        with pytest.raises(ValueError):
            self.calc.calculate_thermal_conductivity_integral(
                self.material, 1.0, 77.0  # 1K is below minimum
            )
    
    def test_thermal_power_calculation(self):
        """Test thermal power calculation using Q = (A/L) * ∫k(T)dT."""
        power = self.calc.calculate_thermal_power(
            self.material, self.rod, 300.0, 77.0
        )
        
        assert isinstance(power, float)
        assert power > 0
        
        # Verify formula: Q = (A/L) * ∫k(T)dT
        k_integral = self.calc.calculate_thermal_conductivity_integral(
            self.material, 77.0, 300.0
        )
        area = self.rod.cross_sectional_area()
        length = self.rod.length
        expected_power = (area / length) * k_integral
        assert abs(power - expected_power) / expected_power < 1e-10
    
    def test_thermal_power_with_different_materials(self):
        """Test thermal power with different materials."""
        power_al = self.calc.calculate_thermal_power(
            "aluminum_6061_t6", self.rod, 300.0, 77.0
        )
        power_cu = self.calc.calculate_thermal_power(
            "copper_ofhc_rrr100", self.rod, 300.0, 77.0
        )
        
        assert isinstance(power_al, float)
        assert isinstance(power_cu, float)
        assert power_al > 0
        assert power_cu > 0
        
        # Copper should have higher thermal power than aluminum
        assert power_cu > power_al
    
    def test_thermal_power_invalid_temperatures(self):
        """Test thermal power with invalid temperatures."""
        with pytest.raises(ValueError):
            self.calc.calculate_thermal_power(
                self.material, self.rod, 77.0, 300.0  # cold > hot
            )
    
    def test_temperature_profile_with_both_temps(self):
        """Test temperature profile with both temperatures given."""
        positions, temperatures = self.calc.calculate_temperature_profile(
            self.material, self.rod, temp_hot=300.0, temp_cold=77.0, num_points=10
        )
        
        assert len(positions) == 10
        assert len(temperatures) == 10
        assert positions[0] == 0
        assert positions[-1] == self.rod.length
        assert temperatures[0] == 300.0
        assert abs(temperatures[-1] - 77.0) < 1.0  # Allow some tolerance for iterative solver
        
        # Temperatures should be monotonically decreasing
        assert all(temperatures[i] >= temperatures[i+1] for i in range(len(temperatures)-1))
    
    def test_temperature_profile_with_power(self):
        """Test temperature profile with thermal power given."""
        # First calculate power for reference
        power = self.calc.calculate_thermal_power(
            self.material, self.rod, 300.0, 77.0
        )
        
        # Now use that power to calculate profile
        positions, temperatures = self.calc.calculate_temperature_profile(
            self.material, self.rod, temp_hot=300.0, thermal_power=power, num_points=10
        )
        
        assert len(positions) == 10
        assert len(temperatures) == 10
        assert temperatures[0] == 300.0
        assert temperatures[-1] < 300.0  # Should drop from hot end
        
        # Temperatures should be monotonically decreasing
        assert all(temperatures[i] >= temperatures[i+1] for i in range(len(temperatures)-1))
    
    def test_temperature_profile_invalid_inputs(self):
        """Test temperature profile with invalid inputs."""
        # Missing temp_hot
        with pytest.raises(ValueError):
            self.calc.calculate_temperature_profile(
                self.material, self.rod, temp_cold=77.0
            )
        
        # Missing both temp_cold and thermal_power
        with pytest.raises(ValueError):
            self.calc.calculate_temperature_profile(
                self.material, self.rod, temp_hot=300.0
            )
        
        # Both temp_cold and thermal_power given
        with pytest.raises(ValueError):
            self.calc.calculate_temperature_profile(
                self.material, self.rod, temp_hot=300.0, temp_cold=77.0, thermal_power=10.0
            )
    
    def test_calculation_summary(self):
        """Test comprehensive calculation summary."""
        summary = self.calc.get_calculation_summary(
            self.material, self.rod, 300.0, 77.0
        )
        
        assert isinstance(summary, dict)
        
        # Check required sections
        assert 'material' in summary
        assert 'geometry' in summary
        assert 'temperatures' in summary
        assert 'thermal_conductivity' in summary
        assert 'results' in summary
        
        # Check material info
        assert summary['material']['id'] == self.material
        assert 'name' in summary['material']
        
        # Check geometry info
        assert summary['geometry']['type'] == 'rod'
        assert summary['geometry']['length_mm'] == 100.0
        assert summary['geometry']['area_mm2'] > 0
        
        # Check temperatures
        assert summary['temperatures']['hot_side_K'] == 300.0
        assert summary['temperatures']['cold_side_K'] == 77.0
        assert summary['temperatures']['delta_T_K'] == 223.0
        
        # Check results
        assert summary['results']['thermal_conductivity_integral_W_K_per_m_K'] > 0
        assert summary['results']['average_thermal_conductivity_W_per_m_K'] > 0
        assert summary['results']['thermal_power_W'] > 0


class TestDifferentMaterials:
    """Test thermal calculations with different materials."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calc = ThermalCalculator()
        self.rod = create_rod(diameter_mm=5, length_mm=50)
    
    def test_copper_high_conductivity(self):
        """Test copper thermal calculations."""
        power_copper = self.calc.calculate_thermal_power(
            "copper_ofhc_rrr100", self.rod, 300.0, 77.0
        )
        
        power_steel = self.calc.calculate_thermal_power(
            "stainless_steel_304", self.rod, 300.0, 77.0
        )
        
        # Copper should have much higher thermal power than steel
        assert power_copper > power_steel * 10
    
    def test_different_geometries(self):
        """Test different geometry types."""
        materials = ["aluminum_6061_t6"]
        
        rod = create_rod(diameter_mm=10, length_mm=100)
        tube = create_tube(outer_diameter_mm=12, wall_thickness_mm=1, length_mm=100)
        bar = create_bar(width_mm=10, thickness_mm=10, length_mm=100)
        
        for material in materials:
            power_rod = self.calc.calculate_thermal_power(material, rod, 300.0, 77.0)
            power_tube = self.calc.calculate_thermal_power(material, tube, 300.0, 77.0)
            power_bar = self.calc.calculate_thermal_power(material, bar, 300.0, 77.0)
            
            # All should be positive
            assert power_rod > 0
            assert power_tube > 0
            assert power_bar > 0
            
            # Bar should have highest power (largest cross-section)
            assert power_bar > power_rod
            assert power_bar > power_tube


class TestEdgeCases:
    """Test edge cases and error conditions."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calc = ThermalCalculator()
    
    def test_very_small_geometry(self):
        """Test very small geometry."""
        wire = create_wire(diameter_mm=0.1, length_mm=10)
        
        power = self.calc.calculate_thermal_power(
            "aluminum_6061_t6", wire, 300.0, 77.0
        )
        
        assert power > 0
        assert power < 0.1  # Should be small for thin wire
    
    def test_very_large_geometry(self):
        """Test large geometry."""
        bar = create_bar(width_mm=100, thickness_mm=50, length_mm=1000)
        
        power = self.calc.calculate_thermal_power(
            "aluminum_6061_t6", bar, 300.0, 77.0
        )
        
        assert power > 10  # Should be large for big bar
    
    def test_small_temperature_difference(self):
        """Test small temperature difference."""
        rod = create_rod(diameter_mm=10, length_mm=100)
        
        power = self.calc.calculate_thermal_power(
            "aluminum_6061_t6", rod, 78.0, 77.0
        )
        
        assert power > 0
        assert power < 1  # Should be small for 1K difference
    
    def test_invalid_material(self):
        """Test with invalid material."""
        rod = create_rod(diameter_mm=10, length_mm=100)
        
        with pytest.raises(ValueError):
            self.calc.calculate_thermal_power(
                "nonexistent_material", rod, 300.0, 77.0
            )


class TestTemperatureProfileValidation:
    """Test that temperature profile solutions satisfy the governing ODE."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calc = ThermalCalculator()
    
    def test_temperature_profile_satisfies_ode_copper(self):
        """Test that temperature profile satisfies dT/dx = -Q/(A*k(T)) for copper."""
        # Test case: copper rod
        rod = create_rod(diameter_mm=10, length_mm=100)
        material = "copper_ofhc_rrr100"
        temp_hot, temp_cold = 300.0, 77.0
        
        # Calculate temperature profile
        positions, temperatures = self.calc.calculate_temperature_profile(
            material, rod, temp_hot=temp_hot, temp_cold=temp_cold, num_points=20
        )
        
        # Calculate thermal power
        power = self.calc.calculate_thermal_power(material, rod, temp_hot, temp_cold)
        area = rod.cross_sectional_area()
        
        # Verify ODE: dT/dx = -Q/(A*k(T))
        # Calculate numerical derivative dT/dx
        for i in range(1, len(positions) - 1):
            # Central difference for dT/dx
            dt_dx_numerical = (temperatures[i+1] - temperatures[i-1]) / (positions[i+1] - positions[i-1])
            
            # Calculate theoretical dT/dx = -Q/(A*k(T))
            k_T = self.calc.calculator.calculate_thermal_conductivity(material, temperatures[i])
            dt_dx_theoretical = -power / (area * k_T)
            
            # Check that numerical and theoretical derivatives match within tolerance
            relative_error = abs(dt_dx_numerical - dt_dx_theoretical) / abs(dt_dx_theoretical)
            assert relative_error < 0.1, f"ODE not satisfied at x={positions[i]:.3f}m: numerical={dt_dx_numerical:.3f}, theoretical={dt_dx_theoretical:.3f}, error={relative_error:.3f}"
    
    def test_temperature_profile_satisfies_ode_aluminum(self):
        """Test that temperature profile satisfies dT/dx = -Q/(A*k(T)) for aluminum."""
        # Test case: aluminum rod
        rod = create_rod(diameter_mm=8, length_mm=50)
        material = "aluminum_6061_t6"
        temp_hot, temp_cold = 300.0, 77.0
        
        # Calculate temperature profile
        positions, temperatures = self.calc.calculate_temperature_profile(
            material, rod, temp_hot=temp_hot, temp_cold=temp_cold, num_points=15
        )
        
        # Calculate thermal power
        power = self.calc.calculate_thermal_power(material, rod, temp_hot, temp_cold)
        area = rod.cross_sectional_area()
        
        # Verify ODE: dT/dx = -Q/(A*k(T))
        for i in range(1, len(positions) - 1):
            dt_dx_numerical = (temperatures[i+1] - temperatures[i-1]) / (positions[i+1] - positions[i-1])
            k_T = self.calc.calculator.calculate_thermal_conductivity(material, temperatures[i])
            dt_dx_theoretical = -power / (area * k_T)
            
            relative_error = abs(dt_dx_numerical - dt_dx_theoretical) / abs(dt_dx_theoretical)
            assert relative_error < 0.1, f"ODE not satisfied at x={positions[i]:.3f}m: error={relative_error:.3f}"
    
    def test_temperature_profile_satisfies_ode_stainless_steel(self):
        """Test that temperature profile satisfies dT/dx = -Q/(A*k(T)) for stainless steel."""
        # Test case: stainless steel tube (lower thermal conductivity)
        tube = create_tube(outer_diameter_mm=20, wall_thickness_mm=2, length_mm=200)
        material = "stainless_steel_304"
        temp_hot, temp_cold = 300.0, 4.2
        
        # Calculate temperature profile
        positions, temperatures = self.calc.calculate_temperature_profile(
            material, tube, temp_hot=temp_hot, temp_cold=temp_cold, num_points=25
        )
        
        # Calculate thermal power
        power = self.calc.calculate_thermal_power(material, tube, temp_hot, temp_cold)
        area = tube.cross_sectional_area()
        
        # Verify ODE: dT/dx = -Q/(A*k(T))
        # Skip points near the ends where numerical derivatives are less accurate
        errors = []
        for i in range(2, len(positions) - 3):  # Skip first/last few points
            dt_dx_numerical = (temperatures[i+1] - temperatures[i-1]) / (positions[i+1] - positions[i-1])
            k_T = self.calc.calculator.calculate_thermal_conductivity(material, temperatures[i])
            dt_dx_theoretical = -power / (area * k_T)
            
            relative_error = abs(dt_dx_numerical - dt_dx_theoretical) / abs(dt_dx_theoretical)
            errors.append(relative_error)
        
        # Check that most points satisfy the ODE within tolerance
        good_points = sum(1 for error in errors if error < 0.2)
        total_points = len(errors)
        success_rate = good_points / total_points
        
        assert success_rate > 0.8, f"ODE not satisfied for {material}: {good_points}/{total_points} points within tolerance"
    
    def test_temperature_profile_with_power_input(self):
        """Test temperature profile when thermal power is specified instead of cold temperature."""
        rod = create_rod(diameter_mm=6, length_mm=75)
        material = "copper_ofhc_rrr100"
        temp_hot = 300.0
        specified_power = 50.0  # Watts
        
        # Calculate temperature profile with specified power
        positions, temperatures = self.calc.calculate_temperature_profile(
            material, rod, temp_hot=temp_hot, thermal_power=specified_power, num_points=15
        )
        
        area = rod.cross_sectional_area()
        
        # Verify ODE: dT/dx = -Q/(A*k(T)) using the specified power
        for i in range(1, len(positions) - 1):
            dt_dx_numerical = (temperatures[i+1] - temperatures[i-1]) / (positions[i+1] - positions[i-1])
            k_T = self.calc.calculator.calculate_thermal_conductivity(material, temperatures[i])
            dt_dx_theoretical = -specified_power / (area * k_T)
            
            relative_error = abs(dt_dx_numerical - dt_dx_theoretical) / abs(dt_dx_theoretical)
            assert relative_error < 0.1, f"ODE not satisfied at x={positions[i]:.3f}m: error={relative_error:.3f}"
    
    def test_boundary_conditions(self):
        """Test that boundary conditions are satisfied."""
        rod = create_rod(diameter_mm=12, length_mm=150)
        material = "aluminum_6061_t6"
        temp_hot, temp_cold = 300.0, 77.0
        
        # Calculate temperature profile
        positions, temperatures = self.calc.calculate_temperature_profile(
            material, rod, temp_hot=temp_hot, temp_cold=temp_cold, num_points=10
        )
        
        # Check boundary conditions
        assert abs(temperatures[0] - temp_hot) < 1e-10, f"Hot boundary not satisfied: {temperatures[0]} != {temp_hot}"
        assert abs(temperatures[-1] - temp_cold) < 5.0, f"Cold boundary not satisfied: {temperatures[-1]} != {temp_cold}"
        
        # Check monotonic decrease
        for i in range(len(temperatures) - 1):
            assert temperatures[i] >= temperatures[i+1], f"Temperature not monotonically decreasing at index {i}"
    
    def test_conservation_of_energy(self):
        """Test that energy conservation is satisfied along the profile."""
        rod = create_rod(diameter_mm=8, length_mm=100)
        material = "copper_ofhc_rrr100"
        temp_hot, temp_cold = 300.0, 77.0
        
        # Calculate temperature profile
        positions, temperatures = self.calc.calculate_temperature_profile(
            material, rod, temp_hot=temp_hot, temp_cold=temp_cold, num_points=20
        )
        
        # Calculate thermal power
        power_expected = self.calc.calculate_thermal_power(material, rod, temp_hot, temp_cold)
        area = rod.cross_sectional_area()
        
        # Check that Q = -A*k*dT/dx is constant along the profile
        powers = []
        for i in range(1, len(positions) - 1):
            dt_dx = (temperatures[i+1] - temperatures[i-1]) / (positions[i+1] - positions[i-1])
            k_T = self.calc.calculator.calculate_thermal_conductivity(material, temperatures[i])
            power_local = -area * k_T * dt_dx
            powers.append(power_local)
        
        # Check that power is approximately constant
        power_mean = np.mean(powers)
        power_std = np.std(powers)
        
        # Power should be close to expected value
        assert abs(power_mean - power_expected) / power_expected < 0.1, f"Mean power {power_mean:.3f} != expected {power_expected:.3f}"
        
        # Power variation should be small (conservation of energy)
        assert power_std / power_mean < 0.1, f"Power variation too large: std/mean = {power_std/power_mean:.3f}"
