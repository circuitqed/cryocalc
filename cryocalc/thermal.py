"""
Thermal conductance and geometry calculations for cryogenic materials.
"""

import math
from typing import Tuple, Optional, Dict, Any
from enum import Enum
from dataclasses import dataclass
from scipy import integrate
import numpy as np

from .calculator import MaterialCalculator


class GeometryType(Enum):
    """Enumeration of supported geometry types."""
    ROD = "rod"
    WIRE = "wire"
    TUBE = "tube"
    BAR = "bar"
    CUSTOM = "custom"


class Geometry:
    """Base class for thermal geometry definitions."""
    
    def __init__(self, length: float, geometry_type: GeometryType = GeometryType.CUSTOM):
        self.length = length
        self.geometry_type = geometry_type
    
    def cross_sectional_area(self) -> float:
        """Calculate cross-sectional area in m²."""
        raise NotImplementedError("Subclasses must implement cross_sectional_area")
    
    def description(self) -> str:
        """Get geometry description."""
        raise NotImplementedError("Subclasses must implement description")


class RodGeometry(Geometry):
    """Rod or wire geometry (circular cross-section)."""
    
    def __init__(self, diameter: float, length: float):
        geometry_type = GeometryType.ROD if diameter >= 0.001 else GeometryType.WIRE
        super().__init__(length, geometry_type)
        self.diameter = diameter
    
    def cross_sectional_area(self) -> float:
        """Calculate cross-sectional area for circular rod/wire."""
        return math.pi * (self.diameter / 2) ** 2
    
    def description(self) -> str:
        """Get geometry description."""
        type_name = "rod" if self.geometry_type == GeometryType.ROD else "wire"
        return f"{type_name}: Ø{self.diameter*1000:.1f}mm × {self.length*1000:.1f}mm"


class TubeGeometry(Geometry):
    """Tube geometry (hollow circular cross-section)."""
    
    def __init__(self, outer_diameter: float, wall_thickness: float, length: float):
        super().__init__(length, GeometryType.TUBE)
        if wall_thickness >= outer_diameter / 2:
            raise ValueError("Wall thickness cannot be >= outer radius")
        self.outer_diameter = outer_diameter
        self.wall_thickness = wall_thickness
    
    def cross_sectional_area(self) -> float:
        """Calculate cross-sectional area for tube wall."""
        outer_radius = self.outer_diameter / 2
        inner_radius = outer_radius - self.wall_thickness
        return math.pi * (outer_radius**2 - inner_radius**2)
    
    def description(self) -> str:
        """Get geometry description."""
        return f"tube: Ø{self.outer_diameter*1000:.1f}mm × {self.wall_thickness*1000:.1f}mm wall × {self.length*1000:.1f}mm"


class BarGeometry(Geometry):
    """Rectangular bar geometry."""
    
    def __init__(self, width: float, thickness: float, length: float):
        super().__init__(length, GeometryType.BAR)
        self.width = width
        self.thickness = thickness
    
    def cross_sectional_area(self) -> float:
        """Calculate cross-sectional area for rectangular bar."""
        return self.width * self.thickness
    
    def description(self) -> str:
        """Get geometry description."""
        return f"bar: {self.width*1000:.1f}mm × {self.thickness*1000:.1f}mm × {self.length*1000:.1f}mm"


class CustomGeometry(Geometry):
    """Custom geometry with specified cross-sectional area."""
    
    def __init__(self, area: float, length: float, description_text: str = "custom geometry"):
        super().__init__(length, GeometryType.CUSTOM)
        self.area = area
        self.description_text = description_text
    
    def cross_sectional_area(self) -> float:
        """Return specified cross-sectional area."""
        return self.area
    
    def description(self) -> str:
        """Get geometry description."""
        return f"{self.description_text}: A={self.area*1e6:.2f}mm² × {self.length*1000:.1f}mm"


class ThermalCalculator:
    """
    Calculator for thermal conductivity integration and thermal resistance analysis.
    
    Provides physically meaningful thermal analysis:
    - Thermal conductivity integration: ∫k(T)dT over temperature ranges
    - Thermal resistance integration: ∫(1/k(T))dT for heat transfer analysis
    """
    
    def __init__(self, material_calculator: Optional[MaterialCalculator] = None):
        """
        Initialize thermal calculator.
        
        Args:
            material_calculator: MaterialCalculator instance. If None, creates new one.
        """
        self.calculator = material_calculator or MaterialCalculator()
    
    def calculate_thermal_conductivity_integral(self, material_id: str, 
                                              temp_low: float, temp_high: float,
                                              num_points: int = 100) -> float:
        """
        Calculate integral of thermal conductivity over temperature range.
        
        ∫[T1 to T2] k(T) dT
        
        Args:
            material_id: Material identifier
            temp_low: Lower temperature bound (K)
            temp_high: Upper temperature bound (K)
            num_points: Number of integration points
            
        Returns:
            Integral value in W·K/m·K
        """
        if temp_low >= temp_high:
            raise ValueError("temp_low must be less than temp_high")
        
        # Validate temperature range
        min_temp, max_temp = self.calculator.database.get_temperature_range(
            material_id, 'thermal_conductivity'
        )
        
        if temp_low < min_temp or temp_high > max_temp:
            raise ValueError(
                f"Temperature range [{temp_low}, {temp_high}]K outside valid range "
                f"[{min_temp}, {max_temp}]K for {material_id}"
            )
        
        # Create temperature array
        temperatures = np.linspace(temp_low, temp_high, num_points)
        
        # Calculate thermal conductivity at each temperature
        conductivities = []
        for temp in temperatures:
            k = self.calculator.calculate_thermal_conductivity(material_id, temp)
            conductivities.append(k)
        
        # Integrate using trapezoidal rule
        integral = np.trapezoid(conductivities, temperatures)
        
        return integral
    
    def calculate_thermal_resistance_integral(self, material_id: str, geometry: Geometry,
                                            temp_low: float, temp_high: float,
                                            num_points: int = 100) -> float:
        """
        Calculate thermal resistance integral for given geometry and temperature range.
        
        R_integral = (L/A) * ∫[T1 to T2] 1/k(T) dT
        
        This is the physically meaningful quantity for thermal analysis.
        
        Args:
            material_id: Material identifier
            geometry: Geometry specification
            temp_low: Lower temperature (K)
            temp_high: Upper temperature (K)
            num_points: Number of integration points
            
        Returns:
            Thermal resistance integral in K/W
        """
        # Validate temperature range
        temp_range = self.calculator.database.get_temperature_range(
            material_id, "thermal_conductivity"
        )
        if temp_low < temp_range[0] or temp_high > temp_range[1]:
            raise ValueError(
                f"Temperature range [{temp_low}, {temp_high}]K outside valid range "
                f"[{temp_range[0]}, {temp_range[1]}]K for {material_id}"
            )
        
        if temp_low >= temp_high:
            raise ValueError("temp_low must be less than temp_high")
        
        # Create temperature array
        temperatures = np.linspace(temp_low, temp_high, num_points)
        
        # Calculate 1/k(T) at each temperature
        inverse_conductivities = []
        for temp in temperatures:
            k = self.calculator.calculate_thermal_conductivity(material_id, temp)
            if k <= 0:
                raise ValueError(f"Invalid thermal conductivity {k} at {temp}K")
            inverse_conductivities.append(1.0 / k)
        
        # Integrate using trapezoidal rule
        resistance_integral = np.trapezoid(inverse_conductivities, temperatures)
        
        # Scale by geometry factor L/A
        area = geometry.cross_sectional_area()
        thermal_resistance_integral = (geometry.length / area) * resistance_integral
        
        return thermal_resistance_integral
    
    def calculate_thermal_power(self, material_id: str, geometry: Geometry,
                               temp_hot: float, temp_cold: float,
                               num_points: int = 100) -> float:
        """
        Calculate thermal power transfer between two temperatures using resistance integral.
        
        For steady-state heat transfer: Q = ΔT / R_thermal
        where R_thermal = (L/A) * ∫[1/k(T)]dT
        
        Args:
            material_id: Material identifier
            geometry: Geometry specification
            temp_hot: Hot side temperature (K)
            temp_cold: Cold side temperature (K)
            num_points: Number of integration points
            
        Returns:
            Thermal power in Watts
        """
        if temp_hot <= temp_cold:
            raise ValueError("temp_hot must be greater than temp_cold")
        
        # Calculate thermal resistance integral
        resistance_integral = self.calculate_thermal_resistance_integral(
            material_id, geometry, temp_cold, temp_hot, num_points
        )
        
        # Calculate power: Q = ΔT / R
        delta_t = temp_hot - temp_cold
        power = delta_t / resistance_integral
        
        return power
    
    def calculate_temperature_profile(self, material_id: str, geometry: Geometry,
                                    temp_hot: float, temp_cold: float,
                                    num_points: int = 50) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculate temperature profile along the length of the geometry.
        
        Args:
            material_id: Material identifier
            geometry: Geometry specification
            temp_hot: Hot end temperature (K)
            temp_cold: Cold end temperature (K)
            num_points: Number of points along length
            
        Returns:
            Tuple of (positions, temperatures) arrays
        """
        # Create position array (0 to length)
        positions = np.linspace(0, geometry.length, num_points)
        
        # For now, use linear approximation
        # TODO: Implement iterative solution for nonlinear k(T)
        temperatures = np.linspace(temp_hot, temp_cold, num_points)
        
        return positions, temperatures
    
    def get_calculation_summary(self, material_id: str, geometry: Geometry,
                               temp_hot: float, temp_cold: float,
                               num_points: int = 100) -> Dict[str, Any]:
        """
        Get comprehensive thermal calculation summary.
        
        Args:
            material_id: Material identifier
            geometry: Geometry specification
            temp_hot: Hot side temperature (K)
            temp_cold: Cold side temperature (K)
            num_points: Number of integration points
            
        Returns:
            Dictionary with calculation results and parameters
        """
        # Get material info
        material_info = self.calculator.database._materials_data[material_id]
        
        # Calculate thermal properties
        resistance_integral = self.calculate_thermal_resistance_integral(
            material_id, geometry, temp_cold, temp_hot, num_points
        )
        k_integral = self.calculate_thermal_conductivity_integral(
            material_id, temp_cold, temp_hot, num_points
        )
        
        # Calculate thermal conductivities at endpoints
        k_hot = self.calculator.calculate_thermal_conductivity(material_id, temp_hot)
        k_cold = self.calculator.calculate_thermal_conductivity(material_id, temp_cold)
        
        summary = {
            'material': {
                'id': material_id,
                'name': material_info['name']
            },
            'geometry': {
                'type': geometry.geometry_type.value,
                'description': geometry.description(),
                'length_mm': geometry.length * 1000,
                'area_mm2': geometry.cross_sectional_area() * 1e6
            },
            'temperatures': {
                'hot_side_K': temp_hot,
                'cold_side_K': temp_cold,
                'delta_T_K': temp_hot - temp_cold
            },
            'thermal_conductivity': {
                'hot_side_W_per_mK': k_hot,
                'cold_side_W_per_mK': k_cold,
                'ratio': k_hot / k_cold if k_cold > 0 else float('inf')
            },
            'results': {
                'thermal_resistance_integral_K_per_W': resistance_integral,
                'thermal_conductivity_integral_W_K_per_m_K': k_integral,
                'average_thermal_conductivity_W_per_m_K': k_integral / (temp_hot - temp_cold)
            }
        }
        
        return summary


# Convenience functions for creating geometries
def create_rod(diameter_mm: float, length_mm: float) -> RodGeometry:
    """Create rod geometry with dimensions in mm."""
    return RodGeometry(diameter=diameter_mm/1000, length=length_mm/1000)

def create_wire(diameter_mm: float, length_mm: float) -> RodGeometry:
    """Create wire geometry with dimensions in mm."""
    return RodGeometry(diameter=diameter_mm/1000, length=length_mm/1000)

def create_tube(outer_diameter_mm: float, wall_thickness_mm: float, 
                length_mm: float) -> TubeGeometry:
    """Create tube geometry with dimensions in mm."""
    return TubeGeometry(
        outer_diameter=outer_diameter_mm/1000,
        wall_thickness=wall_thickness_mm/1000,
        length=length_mm/1000
    )

def create_bar(width_mm: float, thickness_mm: float, length_mm: float) -> BarGeometry:
    """Create bar geometry with dimensions in mm."""
    return BarGeometry(
        width=width_mm/1000,
        thickness=thickness_mm/1000,
        length=length_mm/1000
    )

def create_custom(area_mm2: float, length_mm: float, description: str = "custom") -> CustomGeometry:
    """Create custom geometry with area in mm² and length in mm."""
    return CustomGeometry(
        area=area_mm2/1e6,
        length=length_mm/1000,
        description_text=description
    )
