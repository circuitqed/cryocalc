"""
Tests for the MaterialCalculator class.
"""

import pytest
import math
from cryocalc.calculator import MaterialCalculator
from cryocalc.materials import MaterialDatabase
from cryocalc.properties import PropertyType


class TestMaterialCalculator:
    """Test cases for MaterialCalculator."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calculator = MaterialCalculator()
    
    def test_calculator_initialization(self):
        """Test calculator initialization."""
        assert self.calculator.database is not None
        assert self.calculator.property_calculator is not None
    
    def test_calculate_thermal_conductivity_aluminum(self):
        """Test thermal conductivity calculation for aluminum."""
        # Test aluminum 6061-T6 at liquid nitrogen temperature
        result = self.calculator.calculate_thermal_conductivity("aluminum_6061_t6", 77.0)
        assert isinstance(result, float)
        assert result > 0
        # Aluminum should have reasonable thermal conductivity at 77K
        assert result > 50  # W/m-K
    
    def test_calculate_specific_heat_aluminum(self):
        """Test specific heat calculation for aluminum."""
        result = self.calculator.calculate_specific_heat("aluminum_3003_f", 100.0)
        assert isinstance(result, float)
        assert result > 0
        # Specific heat should be reasonable for aluminum
        assert 100 < result < 2000  # J/kg-K
    
    def test_calculate_youngs_modulus_aluminum(self):
        """Test Young's modulus calculation for aluminum."""
        result = self.calculator.calculate_youngs_modulus("aluminum_5083_o", 200.0)
        assert isinstance(result, float)
        assert result > 0
        # Young's modulus for aluminum should be around 70 GPa
        assert 50 < result < 100  # GPa
    
    def test_calculate_linear_expansion_aluminum(self):
        """Test linear expansion calculation for aluminum."""
        result = self.calculator.calculate_linear_expansion("aluminum_3003_f", 150.0)
        assert isinstance(result, float)
        # Linear expansion can be negative at low temperatures
        assert -1000 < result < 1000  # 10^-5 m/m
    
    def test_temperature_range_validation(self):
        """Test temperature range validation."""
        # Test temperature below minimum
        with pytest.raises(ValueError, match="outside valid range"):
            self.calculator.calculate_thermal_conductivity("aluminum_6061_t6", 1.0)
        
        # Test temperature above maximum
        with pytest.raises(ValueError, match="outside valid range"):
            self.calculator.calculate_thermal_conductivity("aluminum_6061_t6", 500.0)
    
    def test_invalid_material(self):
        """Test handling of invalid material."""
        with pytest.raises(ValueError, match="not found in database"):
            self.calculator.calculate_thermal_conductivity("nonexistent_material", 77.0)
    
    def test_invalid_property(self):
        """Test handling of invalid property."""
        with pytest.raises(ValueError, match="not found for material"):
            self.calculator.calculate_property("aluminum_6061_t6", "nonexistent_property", 77.0)
    
    def test_calculate_temperature_series(self):
        """Test temperature series calculation."""
        result = self.calculator.calculate_temperature_series(
            "aluminum_6061_t6", "thermal_conductivity", (50, 200), 10
        )
        
        assert "temperature" in result
        assert "values" in result
        assert len(result["temperature"]) == 10
        assert len(result["values"]) == 10
        
        # Check that temperatures are in ascending order
        temps = result["temperature"]
        assert all(temps[i] <= temps[i+1] for i in range(len(temps)-1))
        
        # Check that all values are positive (for thermal conductivity)
        values = [v for v in result["values"] if v is not None]
        assert all(v > 0 for v in values)
    
    def test_get_material_summary(self):
        """Test material summary generation."""
        summary = self.calculator.get_material_summary("aluminum_6061_t6")
        
        assert "name" in summary
        assert "material_id" in summary
        assert "properties" in summary
        assert summary["material_id"] == "aluminum_6061_t6"
        assert len(summary["properties"]) > 0
        
        # Check property structure
        for prop_name, prop_info in summary["properties"].items():
            assert "temperature_range" in prop_info
            assert "units" in prop_info
            assert "equation_type" in prop_info
            assert len(prop_info["temperature_range"]) == 2
    
    def test_list_materials_with_property(self):
        """Test listing materials by property type."""
        materials = self.calculator.list_materials_with_property(PropertyType.THERMAL_CONDUCTIVITY)
        
        assert isinstance(materials, list)
        assert len(materials) > 0
        
        for material in materials:
            assert "material_id" in material
            assert "name" in material
            assert isinstance(material["material_id"], str)
            assert isinstance(material["name"], str)
    
    def test_precision_parameter(self):
        """Test precision parameter in calculations."""
        # Test different precision levels
        result_2 = self.calculator.calculate_property("aluminum_6061_t6", "thermal_conductivity", 77.0, precision=2)
        result_6 = self.calculator.calculate_property("aluminum_6061_t6", "thermal_conductivity", 77.0, precision=6)
        
        # Results should be different due to rounding
        assert len(str(result_2).split('.')[-1]) <= 2
        assert len(str(result_6).split('.')[-1]) <= 6
    
    def test_copper_rational_function(self):
        """Test rational function calculation for copper."""
        # Test copper OFHC with rational function
        result = self.calculator.calculate_thermal_conductivity("copper_ofhc_rrr50", 77.0)
        assert isinstance(result, float)
        assert result > 0
        # Copper should have very high thermal conductivity
        assert result > 500  # W/m-K
    
    def test_stainless_steel_properties(self):
        """Test multiple properties for stainless steel."""
        material_id = "stainless_steel_304"
        temp = 100.0
        
        # Test thermal conductivity
        tc = self.calculator.calculate_thermal_conductivity(material_id, temp)
        assert tc > 0
        assert tc < 50  # Stainless steel has low thermal conductivity
        
        # Test specific heat
        sh = self.calculator.calculate_specific_heat(material_id, temp)
        assert sh > 0
        assert 200 < sh < 1000  # Reasonable range for specific heat
    
    def test_property_variants(self):
        """Test property variants (directional properties)."""
        # Test G-10 with directional thermal conductivity
        tc_normal = self.calculator.calculate_thermal_conductivity("fiberglass_epoxy_g10", 100.0, "normal")
        tc_wrap = self.calculator.calculate_thermal_conductivity("fiberglass_epoxy_g10", 100.0, "wrap")
        
        assert tc_normal > 0
        assert tc_wrap > 0
        # Wrap direction should have higher conductivity than normal
        assert tc_wrap > tc_normal
