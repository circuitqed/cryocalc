"""
Main calculator class for cryogenic material property calculations.
"""

from typing import Dict, List, Optional, Union
import math

from .materials import MaterialDatabase
from .properties import PropertyType, PropertyCalculator, EquationType


class MaterialCalculator:
    """
    Main calculator for cryogenic material properties.
    
    Provides methods to calculate thermal conductivity, specific heat, Young's modulus,
    and linear expansion for various materials at cryogenic temperatures.
    """
    
    def __init__(self, database: Optional[MaterialDatabase] = None):
        """
        Initialize the calculator.
        
        Args:
            database: MaterialDatabase instance. If None, creates default database.
        """
        self.database = database or MaterialDatabase()
        self.property_calculator = PropertyCalculator()
    
    def calculate_property(self, material_id: str, property_name: str, 
                          temperature: float, precision: int = 6) -> float:
        """
        Calculate a material property at a given temperature.
        
        Args:
            material_id: Material identifier
            property_name: Property name
            temperature: Temperature in Kelvin
            precision: Number of decimal places for result
            
        Returns:
            Calculated property value
            
        Raises:
            ValueError: If material/property not found or temperature out of range
        """
        # Get property data
        prop_data = self.database.get_material_property(material_id, property_name)
        
        # Validate temperature range
        min_temp, max_temp = self.database.get_temperature_range(material_id, property_name)
        PropertyCalculator.validate_temperature_range(temperature, min_temp, max_temp)
        
        # Get calculation parameters
        equation_type = prop_data['equation_type']
        coefficients = prop_data['coefficients']
        
        # Calculate based on equation type
        if equation_type == "logarithmic_polynomial" or equation_type == EquationType.LOGARITHMIC_POLYNOMIAL.value:
            result = self.property_calculator.logarithmic_polynomial(temperature, coefficients)
        elif equation_type == "polynomial" or equation_type == EquationType.POLYNOMIAL.value:
            result = self.property_calculator.polynomial(temperature, coefficients)
        elif equation_type == "rational" or equation_type == EquationType.RATIONAL.value:
            # For rational functions, coefficients are split between numerator and denominator
            num_coeffs = prop_data.get('numerator_coefficients', coefficients[:len(coefficients)//2])
            den_coeffs = prop_data.get('denominator_coefficients', coefficients[len(coefficients)//2:])
            result = self.property_calculator.rational(temperature, num_coeffs, den_coeffs)
        else:
            raise ValueError(f"Unsupported equation type: {equation_type}")
        
        return round(result, precision)
    
    def calculate_thermal_conductivity(self, material_id: str, temperature: float, 
                                     variant: Optional[str] = None) -> float:
        """
        Calculate thermal conductivity for a material.
        
        Args:
            material_id: Material identifier
            temperature: Temperature in Kelvin
            variant: Property variant (e.g., 'normal', 'wrap' for directional properties)
            
        Returns:
            Thermal conductivity in W/m-K
        """
        property_name = "thermal_conductivity"
        if variant:
            property_name += f"_{variant}"
        
        return self.calculate_property(material_id, property_name, temperature)
    
    def calculate_specific_heat(self, material_id: str, temperature: float) -> float:
        """
        Calculate specific heat for a material.
        
        Args:
            material_id: Material identifier
            temperature: Temperature in Kelvin
            
        Returns:
            Specific heat in J/kg-K
        """
        return self.calculate_property(material_id, "specific_heat", temperature)
    
    def calculate_youngs_modulus(self, material_id: str, temperature: float,
                                variant: Optional[str] = None) -> float:
        """
        Calculate Young's modulus for a material.
        
        Args:
            material_id: Material identifier
            temperature: Temperature in Kelvin
            variant: Property variant (e.g., 'low', 'high' for different temperature ranges)
            
        Returns:
            Young's modulus in GPa
        """
        property_name = "youngs_modulus"
        if variant:
            property_name += f"_{variant}"
        
        return self.calculate_property(material_id, property_name, temperature)
    
    def calculate_linear_expansion(self, material_id: str, temperature: float,
                                  variant: Optional[str] = None) -> float:
        """
        Calculate linear expansion for a material.
        
        Args:
            material_id: Material identifier
            temperature: Temperature in Kelvin
            variant: Property variant (e.g., 'normal', 'wrap', 'a_axis', 'c_axis')
            
        Returns:
            Linear expansion in 10^-5 m/m
        """
        property_name = "linear_expansion"
        if variant:
            property_name += f"_{variant}"
        
        return self.calculate_property(material_id, property_name, temperature)
    
    def calculate_temperature_series(self, material_id: str, property_name: str,
                                   temperature_range: tuple, num_points: int = 50) -> Dict[str, List[float]]:
        """
        Calculate property values over a temperature range.
        
        Args:
            material_id: Material identifier
            property_name: Property name
            temperature_range: (min_temp, max_temp) in Kelvin
            num_points: Number of calculation points
            
        Returns:
            Dictionary with 'temperature' and 'values' lists
        """
        min_temp, max_temp = temperature_range
        
        # Validate against material's valid range
        valid_min, valid_max = self.database.get_temperature_range(material_id, property_name)
        min_temp = max(min_temp, valid_min)
        max_temp = min(max_temp, valid_max)
        
        if min_temp >= max_temp:
            raise ValueError("Invalid temperature range after validation")
        
        # Generate temperature points
        temp_step = (max_temp - min_temp) / (num_points - 1)
        temperatures = [min_temp + i * temp_step for i in range(num_points)]
        
        # Calculate values
        values = []
        for temp in temperatures:
            try:
                value = self.calculate_property(material_id, property_name, temp)
                values.append(value)
            except ValueError:
                values.append(None)  # Skip invalid points
        
        return {
            'temperature': temperatures,
            'values': values
        }
    
    def get_material_summary(self, material_id: str) -> Dict[str, any]:
        """
        Get a summary of available properties for a material.
        
        Args:
            material_id: Material identifier
            
        Returns:
            Dictionary with material information and properties
        """
        info = self.database.get_material_info(material_id)
        
        # Add temperature ranges for each property
        properties_with_ranges = {}
        for prop_name in info['properties']:
            try:
                temp_range = self.database.get_temperature_range(material_id, prop_name)
                prop_data = self.database.get_material_property(material_id, prop_name)
                properties_with_ranges[prop_name] = {
                    'temperature_range': temp_range,
                    'units': prop_data.get('units', 'Unknown'),
                    'equation_type': prop_data.get('equation_type', 'Unknown')
                }
            except ValueError:
                continue
        
        return {
            'name': info['name'],
            'material_id': material_id,
            'properties': properties_with_ranges
        }
    
    def list_materials_with_property(self, property_type: PropertyType) -> List[Dict[str, str]]:
        """
        List all materials that have a specific property type.
        
        Args:
            property_type: Type of property to search for
            
        Returns:
            List of dictionaries with material_id and name
        """
        material_ids = self.database.search_materials_by_property(property_type)
        
        materials = []
        for material_id in material_ids:
            try:
                info = self.database.get_material_info(material_id)
                materials.append({
                    'material_id': material_id,
                    'name': info['name']
                })
            except ValueError:
                continue
        
        return materials
