#!/usr/bin/env python3
"""
Basic usage examples for CryoCalc.

This script demonstrates the fundamental functionality of the CryoCalc package
for calculating cryogenic material properties.
"""

from cryocalc import MaterialCalculator, PropertyType


def main():
    """Demonstrate basic CryoCalc usage."""
    print("CryoCalc - Basic Usage Examples")
    print("=" * 40)
    
    # Initialize the calculator
    calc = MaterialCalculator()
    
    # Example 1: Calculate thermal conductivity
    print("\n1. Thermal Conductivity Calculations")
    print("-" * 35)
    
    materials = ["aluminum_6061_t6", "stainless_steel_304", "copper_ofhc_rrr100"]
    temperature = 77.0  # Liquid nitrogen temperature
    
    for material in materials:
        try:
            tc = calc.calculate_thermal_conductivity(material, temperature)
            info = calc.database.get_material_info(material)
            print(f"{info['name']}: {tc:.2f} W/m-K at {temperature}K")
        except ValueError as e:
            print(f"{material}: Error - {e}")
    
    # Example 2: Calculate specific heat
    print("\n2. Specific Heat Calculations")
    print("-" * 30)
    
    temperature = 100.0
    materials_with_sh = ["aluminum_3003_f", "stainless_steel_304", "copper_ofhc_general"]
    
    for material in materials_with_sh:
        try:
            sh = calc.calculate_specific_heat(material, temperature)
            info = calc.database.get_material_info(material)
            print(f"{info['name']}: {sh:.1f} J/kg-K at {temperature}K")
        except ValueError as e:
            print(f"{material}: Error - {e}")
    
    # Example 3: Temperature series calculation
    print("\n3. Temperature Series Calculation")
    print("-" * 34)
    
    material = "aluminum_6061_t6"
    property_name = "thermal_conductivity"
    temp_range = (50, 200)
    
    data = calc.calculate_temperature_series(material, property_name, temp_range, 10)
    
    print(f"Material: {calc.database.get_material_info(material)['name']}")
    print(f"Property: {property_name}")
    print(f"Temperature range: {temp_range[0]}-{temp_range[1]}K")
    print("\nTemperature (K) | Property Value")
    print("-" * 35)
    
    for temp, value in zip(data['temperature'], data['values']):
        if value is not None:
            print(f"{temp:8.1f}      | {value:8.2f}")
    
    # Example 4: Material summary
    print("\n4. Material Summary")
    print("-" * 19)
    
    material = "stainless_steel_304"
    summary = calc.get_material_summary(material)
    
    print(f"Material: {summary['name']}")
    print(f"ID: {summary['material_id']}")
    print("Available properties:")
    
    for prop_name, prop_info in summary['properties'].items():
        temp_range = prop_info['temperature_range']
        units = prop_info['units']
        print(f"  - {prop_name}: {temp_range[0]}-{temp_range[1]}K ({units})")
    
    # Example 5: List materials by property
    print("\n5. Materials with Thermal Conductivity Data")
    print("-" * 42)
    
    materials = calc.list_materials_with_property(PropertyType.THERMAL_CONDUCTIVITY)
    
    for material in materials[:5]:  # Show first 5
        print(f"  - {material['material_id']}: {material['name']}")
    
    if len(materials) > 5:
        print(f"  ... and {len(materials) - 5} more materials")


if __name__ == "__main__":
    main()
