"""
Material database management for cryogenic property calculations.
"""

import json
import os
from typing import Dict, List, Optional, Any
from pathlib import Path

from .properties import PropertyType, EquationType


class MaterialDatabase:
    """
    Database of cryogenic material properties and calculation parameters.
    """
    
    def __init__(self, data_file: Optional[str] = None):
        """
        Initialize the material database.
        
        Args:
            data_file: Path to JSON data file. If None, uses default materials.json
        """
        if data_file is None:
            # Use default data file in package
            package_dir = Path(__file__).parent
            data_file = package_dir / "data" / "materials.json"
        
        self.data_file = Path(data_file)
        self._materials_data = {}
        self.load_materials()
    
    def load_materials(self) -> None:
        """Load materials data from JSON file."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self._materials_data = data.get('materials', {})
        except FileNotFoundError:
            raise FileNotFoundError(f"Materials data file not found: {self.data_file}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in materials data file: {e}")
    
    def get_available_materials(self) -> List[str]:
        """
        Get list of available material identifiers.
        
        Returns:
            List of material IDs
        """
        return list(self._materials_data.keys())
    
    def get_material_info(self, material_id: str) -> Dict[str, Any]:
        """
        Get basic information about a material.
        
        Args:
            material_id: Material identifier
            
        Returns:
            Dictionary with material name and available properties
            
        Raises:
            ValueError: If material not found
        """
        if material_id not in self._materials_data:
            raise ValueError(f"Material '{material_id}' not found in database")
        
        material = self._materials_data[material_id]
        return {
            'name': material.get('name', material_id),
            'properties': list(material.get('properties', {}).keys())
        }
    
    def get_material_property(self, material_id: str, property_name: str) -> Dict[str, Any]:
        """
        Get property data for a specific material and property.
        
        Args:
            material_id: Material identifier
            property_name: Property name
            
        Returns:
            Dictionary with property calculation parameters
            
        Raises:
            ValueError: If material or property not found
        """
        if material_id not in self._materials_data:
            raise ValueError(f"Material '{material_id}' not found in database")
        
        material = self._materials_data[material_id]
        properties = material.get('properties', {})
        
        if property_name not in properties:
            available = list(properties.keys())
            raise ValueError(
                f"Property '{property_name}' not found for material '{material_id}'. "
                f"Available properties: {available}"
            )
        
        return properties[property_name]
    
    def search_materials_by_property(self, property_type) -> List[str]:
        """
        Find materials that have data for a specific property type.
        
        Args:
            property_type: Type of property to search for (PropertyType enum or string)
            
        Returns:
            List of material IDs that have the specified property
        """
        matching_materials = []
        # Handle both PropertyType enum and string inputs
        if hasattr(property_type, 'value'):
            property_name = property_type.value
        else:
            property_name = property_type
        
        for material_id, material_data in self._materials_data.items():
            properties = material_data.get('properties', {})
            # Check for exact match or partial match (for properties with variants)
            for prop_name in properties.keys():
                if prop_name == property_name or prop_name.startswith(property_name):
                    matching_materials.append(material_id)
                    break
        
        return matching_materials
    
    def get_temperature_range(self, material_id: str, property_name: str) -> tuple:
        """
        Get the valid temperature range for a material property.
        
        Args:
            material_id: Material identifier
            property_name: Property name
            
        Returns:
            Tuple of (min_temp, max_temp) in Kelvin
        """
        prop_data = self.get_material_property(material_id, property_name)
        temp_range = prop_data.get('temperature_range', [4, 300])
        return tuple(temp_range)
    
    def validate_calculation_parameters(self, material_id: str, property_name: str) -> bool:
        """
        Validate that all required parameters are present for calculation.
        
        Args:
            material_id: Material identifier
            property_name: Property name
            
        Returns:
            True if parameters are valid, False otherwise
        """
        try:
            prop_data = self.get_material_property(material_id, property_name)
            
            # Check required fields
            required_fields = ['equation_type', 'temperature_range', 'units']
            for field in required_fields:
                if field not in prop_data:
                    return False
            
            # Validate equation type
            equation_type = prop_data['equation_type']
            valid_equation_types = [e.value for e in EquationType] + ["logarithmic_polynomial", "polynomial", "rational"]
            if equation_type not in valid_equation_types:
                return False
            
            # Validate coefficients based on equation type
            if equation_type == "rational":
                # For rational functions, check for either coefficients or separate num/den coefficients
                has_coefficients = 'coefficients' in prop_data and isinstance(prop_data['coefficients'], list)
                has_separate_coeffs = ('numerator_coefficients' in prop_data and 
                                     'denominator_coefficients' in prop_data and
                                     isinstance(prop_data['numerator_coefficients'], list) and
                                     isinstance(prop_data['denominator_coefficients'], list))
                if not (has_coefficients or has_separate_coeffs):
                    return False
            else:
                # For other equation types, check for coefficients
                if 'coefficients' not in prop_data:
                    return False
                coefficients = prop_data['coefficients']
                if not isinstance(coefficients, list) or len(coefficients) == 0:
                    return False
            
            # Validate temperature range
            temp_range = prop_data['temperature_range']
            if not isinstance(temp_range, list) or len(temp_range) != 2:
                return False
            if temp_range[0] >= temp_range[1]:
                return False
            
            return True
            
        except (KeyError, ValueError):
            return False
    
    def add_material(self, material_id: str, material_data: Dict[str, Any]) -> None:
        """
        Add a new material to the database.
        
        Args:
            material_id: Unique identifier for the material
            material_data: Material data dictionary
        """
        self._materials_data[material_id] = material_data
    
    def save_materials(self, output_file: Optional[str] = None) -> None:
        """
        Save materials data to JSON file.
        
        Args:
            output_file: Output file path. If None, saves to original data file
        """
        output_path = Path(output_file) if output_file else self.data_file
        
        data = {'materials': self._materials_data}
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
