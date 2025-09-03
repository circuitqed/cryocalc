#!/usr/bin/env python3
"""
Example of adding custom materials to CryoCalc.

This script demonstrates how to extend the material database
with custom material data.
"""

import json
import tempfile
from pathlib import Path
from cryocalc import MaterialCalculator, MaterialDatabase


def create_custom_material_data():
    """Create example custom material data."""
    custom_materials = {
        "materials": {
            "custom_aluminum_alloy": {
                "name": "Custom Aluminum Alloy",
                "properties": {
                    "thermal_conductivity": {
                        "equation_type": "polynomial",
                        "coefficients": [50.0, 0.5, -0.001, 1e-6],
                        "temperature_range": [10, 300],
                        "units": "W/m-K"
                    },
                    "specific_heat": {
                        "equation_type": "polynomial",
                        "coefficients": [800.0, 2.0, 0.01],
                        "temperature_range": [10, 300],
                        "units": "J/kg-K"
                    }
                }
            },
            "custom_composite": {
                "name": "Custom Carbon Fiber Composite",
                "properties": {
                    "thermal_conductivity_longitudinal": {
                        "equation_type": "logarithmic_polynomial",
                        "coefficients": [1.5, -0.5, 0.1],
                        "temperature_range": [20, 300],
                        "units": "W/m-K"
                    },
                    "thermal_conductivity_transverse": {
                        "equation_type": "logarithmic_polynomial",
                        "coefficients": [0.5, -0.2, 0.05],
                        "temperature_range": [20, 300],
                        "units": "W/m-K"
                    },
                    "youngs_modulus": {
                        "equation_type": "polynomial",
                        "coefficients": [150.0, 0.1, -0.0001],
                        "temperature_range": [20, 300],
                        "units": "GPa"
                    }
                }
            }
        }
    }
    return custom_materials


def demonstrate_custom_database():
    """Demonstrate using a custom material database."""
    print("Custom Material Database Example")
    print("=" * 35)
    
    # Create custom material data
    custom_data = create_custom_material_data()
    
    # Save to temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(custom_data, f, indent=2)
        temp_file = f.name
    
    try:
        # Load custom database
        custom_db = MaterialDatabase(temp_file)
        calc = MaterialCalculator(database=custom_db)
        
        print("\nCustom materials loaded:")
        materials = calc.database.get_available_materials()
        for material_id in materials:
            info = calc.database.get_material_info(material_id)
            print(f"  - {material_id}: {info['name']}")
        
        # Test calculations with custom materials
        print("\nTesting custom material calculations:")
        
        # Custom aluminum alloy
        material_id = "custom_aluminum_alloy"
        temp = 100.0
        
        tc = calc.calculate_thermal_conductivity(material_id, temp)
        sh = calc.calculate_specific_heat(material_id, temp)
        
        print(f"\nCustom Aluminum Alloy at {temp}K:")
        print(f"  Thermal Conductivity: {tc:.2f} W/m-K")
        print(f"  Specific Heat: {sh:.1f} J/kg-K")
        
        # Custom composite with directional properties
        material_id = "custom_composite"
        temp = 200.0
        
        tc_long = calc.calculate_thermal_conductivity(material_id, temp, "longitudinal")
        tc_trans = calc.calculate_thermal_conductivity(material_id, temp, "transverse")
        ym = calc.calculate_youngs_modulus(material_id, temp)
        
        print(f"\nCustom Carbon Fiber Composite at {temp}K:")
        print(f"  Thermal Conductivity (Longitudinal): {tc_long:.3f} W/m-K")
        print(f"  Thermal Conductivity (Transverse): {tc_trans:.3f} W/m-K")
        print(f"  Young's Modulus: {ym:.1f} GPa")
        
    finally:
        # Clean up temporary file
        Path(temp_file).unlink(missing_ok=True)


def demonstrate_adding_material_to_existing_db():
    """Demonstrate adding a material to existing database."""
    print("\nAdding Material to Existing Database")
    print("=" * 38)
    
    # Start with default database
    calc = MaterialCalculator()
    
    # Define new material
    new_material_data = {
        "name": "Experimental Superconductor",
        "properties": {
            "thermal_conductivity": {
                "equation_type": "polynomial",
                "coefficients": [0.1, 0.01, -1e-5],
                "temperature_range": [4, 100],
                "units": "W/m-K"
            },
            "specific_heat": {
                "equation_type": "logarithmic_polynomial",
                "coefficients": [2.0, -1.0, 0.5],
                "temperature_range": [4, 100],
                "units": "J/kg-K"
            }
        }
    }
    
    # Add to database
    calc.database.add_material("experimental_superconductor", new_material_data)
    
    print("Added experimental superconductor to database")
    
    # Test the new material
    material_id = "experimental_superconductor"
    temp = 20.0
    
    tc = calc.calculate_thermal_conductivity(material_id, temp)
    sh = calc.calculate_specific_heat(material_id, temp)
    
    print(f"\nExperimental Superconductor at {temp}K:")
    print(f"  Thermal Conductivity: {tc:.4f} W/m-K")
    print(f"  Specific Heat: {sh:.2f} J/kg-K")
    
    # Show material summary
    summary = calc.get_material_summary(material_id)
    print(f"\nMaterial Summary:")
    print(f"  Name: {summary['name']}")
    print(f"  Properties: {list(summary['properties'].keys())}")


def validate_custom_material():
    """Demonstrate material validation."""
    print("\nMaterial Validation Example")
    print("=" * 29)
    
    calc = MaterialCalculator()
    
    # Valid material
    valid_material = {
        "name": "Valid Test Material",
        "properties": {
            "thermal_conductivity": {
                "equation_type": "polynomial",
                "coefficients": [10.0, 0.1],
                "temperature_range": [10, 300],
                "units": "W/m-K"
            }
        }
    }
    
    calc.database.add_material("valid_test", valid_material)
    is_valid = calc.database.validate_calculation_parameters("valid_test", "thermal_conductivity")
    print(f"Valid material validation: {is_valid}")
    
    # Invalid material (missing required fields)
    invalid_material = {
        "name": "Invalid Test Material",
        "properties": {
            "thermal_conductivity": {
                "equation_type": "polynomial",
                # Missing coefficients, temperature_range, units
            }
        }
    }
    
    calc.database.add_material("invalid_test", invalid_material)
    is_valid = calc.database.validate_calculation_parameters("invalid_test", "thermal_conductivity")
    print(f"Invalid material validation: {is_valid}")


def main():
    """Run all custom material examples."""
    print("CryoCalc - Custom Material Examples")
    print("=" * 37)
    
    try:
        demonstrate_custom_database()
        demonstrate_adding_material_to_existing_db()
        validate_custom_material()
        
        print("\nCustom material examples completed successfully!")
        
    except Exception as e:
        print(f"Error in custom material examples: {e}")


if __name__ == "__main__":
    main()
