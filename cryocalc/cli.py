"""
Command-line interface for CryoCalc.
"""

import argparse
import sys
from typing import Optional

from .calculator import MaterialCalculator
from .properties import PropertyType


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="CryoCalc - Cryogenic Material Property Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  cryocalc list-materials
  cryocalc calculate aluminum_6061_t6 thermal_conductivity 77
  cryocalc info stainless_steel_304
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List materials command
    list_parser = subparsers.add_parser('list-materials', help='List available materials')
    list_parser.add_argument('--property', choices=[p.value for p in PropertyType],
                            help='Filter by property type')
    
    # Material info command
    info_parser = subparsers.add_parser('info', help='Show material information')
    info_parser.add_argument('material', help='Material identifier')
    
    # Calculate command
    calc_parser = subparsers.add_parser('calculate', help='Calculate material property')
    calc_parser.add_argument('material', help='Material identifier')
    calc_parser.add_argument('property', help='Property name')
    calc_parser.add_argument('temperature', type=float, help='Temperature in Kelvin')
    calc_parser.add_argument('--variant', help='Property variant (if applicable)')
    calc_parser.add_argument('--precision', type=int, default=6, help='Decimal precision')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        calculator = MaterialCalculator()
        
        if args.command == 'list-materials':
            if args.property:
                prop_type = PropertyType(args.property)
                materials = calculator.list_materials_with_property(prop_type)
                print(f"\nMaterials with {args.property}:")
                for material in materials:
                    print(f"  {material['material_id']}: {material['name']}")
            else:
                materials = calculator.database.get_available_materials()
                print("\nAvailable materials:")
                for material_id in sorted(materials):
                    info = calculator.database.get_material_info(material_id)
                    print(f"  {material_id}: {info['name']}")
        
        elif args.command == 'info':
            summary = calculator.get_material_summary(args.material)
            print(f"\nMaterial: {summary['name']}")
            print(f"ID: {summary['material_id']}")
            print("\nAvailable properties:")
            for prop_name, prop_info in summary['properties'].items():
                temp_range = prop_info['temperature_range']
                units = prop_info['units']
                print(f"  {prop_name}: {temp_range[0]}-{temp_range[1]}K ({units})")
        
        elif args.command == 'calculate':
            if args.variant:
                property_name = f"{args.property}_{args.variant}"
            else:
                property_name = args.property
            
            result = calculator.calculate_property(
                args.material, property_name, args.temperature, args.precision
            )
            
            # Get units
            prop_data = calculator.database.get_material_property(args.material, property_name)
            units = prop_data.get('units', '')
            
            print(f"\nResult: {result} {units}")
            print(f"Material: {args.material}")
            print(f"Property: {property_name}")
            print(f"Temperature: {args.temperature} K")
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
