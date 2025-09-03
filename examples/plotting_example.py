#!/usr/bin/env python3
"""
Plotting examples for CryoCalc.

This script demonstrates how to create plots of material properties
vs temperature using matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np
from cryocalc import MaterialCalculator


def plot_thermal_conductivity_comparison():
    """Plot thermal conductivity vs temperature for multiple materials."""
    calc = MaterialCalculator()
    
    # Materials to compare
    materials = {
        "aluminum_6061_t6": "Aluminum 6061-T6",
        "stainless_steel_304": "Stainless Steel 304",
        "copper_ofhc_rrr100": "Copper OFHC (RRR=100)"
    }
    
    plt.figure(figsize=(10, 6))
    
    for material_id, name in materials.items():
        try:
            # Get valid temperature range
            temp_range = calc.database.get_temperature_range(material_id, "thermal_conductivity")
            
            # Calculate thermal conductivity over temperature range
            data = calc.calculate_temperature_series(
                material_id, "thermal_conductivity", temp_range, 50
            )
            
            # Filter out None values
            temps = []
            values = []
            for t, v in zip(data['temperature'], data['values']):
                if v is not None:
                    temps.append(t)
                    values.append(v)
            
            plt.plot(temps, values, label=name, linewidth=2)
            
        except ValueError as e:
            print(f"Error plotting {material_id}: {e}")
    
    plt.xlabel('Temperature (K)')
    plt.ylabel('Thermal Conductivity (W/m-K)')
    plt.title('Thermal Conductivity vs Temperature')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.show()


def plot_aluminum_properties():
    """Plot multiple properties for aluminum 6061-T6."""
    calc = MaterialCalculator()
    material_id = "aluminum_6061_t6"
    
    # Properties to plot
    properties = {
        "thermal_conductivity": ("Thermal Conductivity", "W/m-K"),
        "specific_heat": ("Specific Heat", "J/kg-K"),
        "youngs_modulus": ("Young's Modulus", "GPa"),
        "linear_expansion": ("Linear Expansion", "10⁻⁵ m/m")
    }
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    for i, (prop_name, (title, units)) in enumerate(properties.items()):
        try:
            # Get temperature range for this property
            temp_range = calc.database.get_temperature_range(material_id, prop_name)
            
            # Calculate property values
            data = calc.calculate_temperature_series(
                material_id, prop_name, temp_range, 50
            )
            
            # Filter out None values
            temps = []
            values = []
            for t, v in zip(data['temperature'], data['values']):
                if v is not None:
                    temps.append(t)
                    values.append(v)
            
            axes[i].plot(temps, values, 'b-', linewidth=2)
            axes[i].set_xlabel('Temperature (K)')
            axes[i].set_ylabel(f'{title} ({units})')
            axes[i].set_title(f'{title} vs Temperature')
            axes[i].grid(True, alpha=0.3)
            
        except ValueError as e:
            axes[i].text(0.5, 0.5, f'Data not available\n{e}', 
                        transform=axes[i].transAxes, ha='center', va='center')
            axes[i].set_title(f'{title} vs Temperature')
    
    plt.tight_layout()
    plt.suptitle('Aluminum 6061-T6 Properties', y=1.02, fontsize=14)
    plt.show()


def plot_directional_properties():
    """Plot directional properties for G-10 fiberglass."""
    calc = MaterialCalculator()
    material_id = "fiberglass_epoxy_g10"
    
    # Directional thermal conductivity
    directions = {
        "normal": "Normal Direction",
        "wrap": "Wrap Direction"
    }
    
    plt.figure(figsize=(10, 6))
    
    for direction, label in directions.items():
        try:
            prop_name = f"thermal_conductivity_{direction}"
            temp_range = calc.database.get_temperature_range(material_id, prop_name)
            
            data = calc.calculate_temperature_series(
                material_id, prop_name, temp_range, 50
            )
            
            # Filter out None values
            temps = []
            values = []
            for t, v in zip(data['temperature'], data['values']):
                if v is not None:
                    temps.append(t)
                    values.append(v)
            
            plt.plot(temps, values, label=label, linewidth=2)
            
        except ValueError as e:
            print(f"Error plotting {direction}: {e}")
    
    plt.xlabel('Temperature (K)')
    plt.ylabel('Thermal Conductivity (W/m-K)')
    plt.title('G-10 Fiberglass Thermal Conductivity (Directional)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.show()


def main():
    """Run all plotting examples."""
    print("CryoCalc - Plotting Examples")
    print("=" * 30)
    
    try:
        print("\n1. Thermal conductivity comparison...")
        plot_thermal_conductivity_comparison()
        
        print("\n2. Aluminum properties overview...")
        plot_aluminum_properties()
        
        print("\n3. Directional properties (G-10)...")
        plot_directional_properties()
        
    except ImportError:
        print("Error: matplotlib is required for plotting examples.")
        print("Install with: pip install matplotlib")
    except Exception as e:
        print(f"Error creating plots: {e}")


if __name__ == "__main__":
    main()
