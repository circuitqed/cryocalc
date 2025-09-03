"""
Tests for the MaterialDatabase class.
"""

import pytest
import json
import tempfile
from pathlib import Path

from cryocalc.materials import MaterialDatabase
from cryocalc.properties import PropertyType


class TestMaterialDatabase:
    """Test cases for MaterialDatabase."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.database = MaterialDatabase()
    
    def test_database_initialization(self):
        """Test database initialization."""
        assert self.database._materials_data is not None
        assert len(self.database._materials_data) > 0
    
    def test_get_available_materials(self):
        """Test getting available materials."""
        materials = self.database.get_available_materials()
        assert isinstance(materials, list)
        assert len(materials) > 0
        assert "aluminum_6061_t6" in materials
        assert "stainless_steel_304" in materials
    
    def test_get_material_info(self):
        """Test getting material information."""
        info = self.database.get_material_info("aluminum_6061_t6")
        
        assert "name" in info
        assert "properties" in info
        assert isinstance(info["properties"], list)
        assert len(info["properties"]) > 0
        assert "thermal_conductivity" in info["properties"]
    
    def test_get_material_info_invalid(self):
        """Test getting info for invalid material."""
        with pytest.raises(ValueError, match="not found in database"):
            self.database.get_material_info("nonexistent_material")
    
    def test_get_material_property(self):
        """Test getting material property data."""
        prop_data = self.database.get_material_property("aluminum_6061_t6", "thermal_conductivity")
        
        assert "equation_type" in prop_data
        assert "coefficients" in prop_data
        assert "temperature_range" in prop_data
        assert "units" in prop_data
        assert isinstance(prop_data["coefficients"], list)
        assert len(prop_data["coefficients"]) > 0
    
    def test_get_material_property_invalid(self):
        """Test getting invalid property."""
        with pytest.raises(ValueError, match="not found for material"):
            self.database.get_material_property("aluminum_6061_t6", "nonexistent_property")
    
    def test_search_materials_by_property(self):
        """Test searching materials by property type."""
        materials = self.database.search_materials_by_property(PropertyType.THERMAL_CONDUCTIVITY)
        
        assert isinstance(materials, list)
        assert len(materials) > 0
        assert "aluminum_6061_t6" in materials
        assert "stainless_steel_304" in materials
    
    def test_get_temperature_range(self):
        """Test getting temperature range."""
        temp_range = self.database.get_temperature_range("aluminum_6061_t6", "thermal_conductivity")
        
        assert isinstance(temp_range, tuple)
        assert len(temp_range) == 2
        assert temp_range[0] < temp_range[1]
        assert temp_range[0] >= 0  # Temperature should be positive
    
    def test_validate_calculation_parameters(self):
        """Test parameter validation."""
        # Valid parameters
        assert self.database.validate_calculation_parameters("aluminum_6061_t6", "thermal_conductivity")
        
        # Invalid material
        assert not self.database.validate_calculation_parameters("nonexistent", "thermal_conductivity")
        
        # Invalid property
        assert not self.database.validate_calculation_parameters("aluminum_6061_t6", "nonexistent")
    
    def test_add_material(self):
        """Test adding new material."""
        new_material = {
            "name": "Test Material",
            "properties": {
                "thermal_conductivity": {
                    "equation_type": "polynomial",
                    "coefficients": [1.0, 0.1, 0.01],
                    "temperature_range": [10, 300],
                    "units": "W/m-K"
                }
            }
        }
        
        self.database.add_material("test_material", new_material)
        
        # Verify material was added
        materials = self.database.get_available_materials()
        assert "test_material" in materials
        
        info = self.database.get_material_info("test_material")
        assert info["name"] == "Test Material"
    
    def test_save_and_load_materials(self):
        """Test saving and loading materials."""
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name
        
        try:
            # Save current materials
            self.database.save_materials(temp_file)
            
            # Load from temporary file
            new_database = MaterialDatabase(temp_file)
            
            # Compare materials
            original_materials = set(self.database.get_available_materials())
            loaded_materials = set(new_database.get_available_materials())
            
            assert original_materials == loaded_materials
            
        finally:
            # Clean up
            Path(temp_file).unlink(missing_ok=True)
    
    def test_invalid_json_file(self):
        """Test handling of invalid JSON file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write("invalid json content")
            temp_file = f.name
        
        try:
            with pytest.raises(ValueError, match="Invalid JSON"):
                MaterialDatabase(temp_file)
        finally:
            Path(temp_file).unlink(missing_ok=True)
    
    def test_missing_file(self):
        """Test handling of missing file."""
        with pytest.raises(FileNotFoundError, match="not found"):
            MaterialDatabase("nonexistent_file.json")
