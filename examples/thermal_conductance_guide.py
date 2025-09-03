#!/usr/bin/env python3
"""
Thermal Conductance Analysis Guide
==================================

This example demonstrates the thermal analysis capabilities of CryoCalc,
including thermal conductivity integration, conductance calculations,
and geometry-specific heat transfer analysis.

Author: CryoCalc Development Team
"""

from cryocalc import (
    ThermalConductanceCalculator,
    create_rod, create_wire, create_tube, create_bar, create_custom
)
import numpy as np

def main():
    print("🌡️  CryoCalc Thermal Conductance Analysis Guide")
    print("=" * 60)
    
    # Initialize thermal calculator
    calc = ThermalConductanceCalculator()
    
    # Example 1: Basic Thermal Conductance
    print("\n1. Basic Thermal Conductance Calculation")
    print("-" * 45)
    
    # Create a copper rod
    copper_rod = create_rod(diameter_mm=6, length_mm=100)
    material = "copper_ofhc_rrr100"
    
    # Calculate conductance and power
    conductance = calc.calculate_thermal_conductance(material, copper_rod, 77, 300)
    power = calc.calculate_thermal_power(material, copper_rod, 300, 77)
    resistance = 1.0 / conductance
    
    print(f"Material: Copper OFHC RRR=100")
    print(f"Geometry: {copper_rod.description()}")
    print(f"Temperature range: 77K to 300K")
    print(f"Thermal conductance: {conductance:.4f} W/K")
    print(f"Thermal power (300K→77K): {power:.2f} W")
    print(f"Thermal resistance: {resistance:.2f} K/W")
    
    # Example 2: Material Comparison
    print("\n2. Material Comparison")
    print("-" * 30)
    
    # Compare different materials with same geometry
    rod = create_rod(diameter_mm=5, length_mm=50)
    materials = [
        ("copper_ofhc_rrr100", "Copper OFHC RRR=100"),
        ("aluminum_6061_t6", "Aluminum 6061-T6"),
        ("stainless_steel_304", "Stainless Steel 304")
    ]
    
    print(f"Geometry: {rod.description()}")
    print(f"Temperature: 300K → 77K")
    print()
    print("Material Comparison:")
    print("Material                | Power (W) | Conductance (W/K)")
    print("-" * 55)
    
    for mat_id, mat_name in materials:
        power = calc.calculate_thermal_power(mat_id, rod, 300, 77)
        conductance = calc.calculate_thermal_conductance(mat_id, rod, 77, 300)
        print(f"{mat_name:22s} | {power:8.3f} | {conductance:12.6f}")
    
    # Example 3: Geometry Comparison
    print("\n3. Geometry Comparison")
    print("-" * 25)
    
    material = "aluminum_6061_t6"
    geometries = [
        ("Rod", create_rod(diameter_mm=8, length_mm=100)),
        ("Wire", create_wire(diameter_mm=1, length_mm=100)),
        ("Tube", create_tube(outer_diameter_mm=10, wall_thickness_mm=1, length_mm=100)),
        ("Bar", create_bar(width_mm=8, thickness_mm=4, length_mm=100))
    ]
    
    print(f"Material: Aluminum 6061-T6")
    print(f"Temperature: 300K → 77K")
    print()
    print("Geometry Comparison:")
    print("Type | Description                    | Area (mm²) | Power (W)")
    print("-" * 65)
    
    for name, geom in geometries:
        power = calc.calculate_thermal_power(material, geom, 300, 77)
        area = geom.cross_sectional_area() * 1e6  # Convert to mm²
        print(f"{name:4s} | {geom.description():30s} | {area:9.2f} | {power:8.3f}")
    
    # Example 4: Thermal Conductivity Integration
    print("\n4. Thermal Conductivity Integration")
    print("-" * 38)
    
    material = "copper_ofhc_rrr100"
    temp_ranges = [
        (4, 77, "Liquid He to LN₂"),
        (77, 300, "LN₂ to Room Temp"),
        (4, 300, "Full Cryogenic Range")
    ]
    
    print(f"Material: Copper OFHC RRR=100")
    print()
    print("Thermal Conductivity Integration:")
    print("Range (K)      | Integral (W·K/m·K) | Avg k (W/m·K) | Description")
    print("-" * 75)
    
    for t_low, t_high, desc in temp_ranges:
        integral = calc.calculate_thermal_conductivity_integral(material, t_low, t_high)
        avg_k = integral / (t_high - t_low)
        print(f"{t_low:3.0f}K → {t_high:3.0f}K | {integral:15.1f} | {avg_k:11.1f} | {desc}")
    
    # Example 5: Cryogenic Transfer Line Analysis
    print("\n5. Cryogenic Transfer Line Analysis")
    print("-" * 40)
    
    # Stainless steel vacuum-jacketed transfer line
    material = "stainless_steel_304"
    transfer_line = create_tube(
        outer_diameter_mm=25.4,    # 1 inch outer diameter
        wall_thickness_mm=1.6,     # 1/16 inch wall
        length_mm=1000             # 1 meter length
    )
    
    summary = calc.get_calculation_summary(material, transfer_line, 300.0, 4.2)
    
    print("Analysis: Vacuum-Jacketed Transfer Line")
    print(f"Material: {summary['material']['name']}")
    print(f"Geometry: {summary['geometry']['description']}")
    print(f"Length: {summary['geometry']['length_mm']:.0f} mm")
    print(f"Cross-sectional area: {summary['geometry']['area_mm2']:.1f} mm²")
    print()
    print("Temperature Analysis:")
    print(f"  Hot side: {summary['temperatures']['hot_side_K']:.1f} K")
    print(f"  Cold side: {summary['temperatures']['cold_side_K']:.1f} K")
    print(f"  ΔT: {summary['temperatures']['delta_T_K']:.1f} K")
    print()
    print("Thermal Conductivity:")
    print(f"  @ {summary['temperatures']['hot_side_K']:.1f}K: {summary['thermal_conductivity']['hot_side_W_per_mK']:.3f} W/m·K")
    print(f"  @ {summary['temperatures']['cold_side_K']:.1f}K: {summary['thermal_conductivity']['cold_side_W_per_mK']:.3f} W/m·K")
    print(f"  Ratio: {summary['thermal_conductivity']['ratio']:.1f}:1")
    print()
    print("Thermal Performance:")
    print(f"  Conductance: {summary['results']['thermal_conductance_W_per_K']:.6f} W/K")
    print(f"  Resistance: {summary['results']['thermal_resistance_K_per_W']:.1f} K/W")
    print(f"  Heat leak: {summary['results']['thermal_power_W']:.3f} W")
    print(f"  Heat flux: {summary['results']['heat_flux_W_per_m2']:.0f} W/m²")
    
    # Example 6: Temperature-Dependent Analysis
    print("\n6. Temperature-Dependent Analysis")
    print("-" * 35)
    
    material = "aluminum_6061_t6"
    rod = create_rod(diameter_mm=6, length_mm=200)
    
    # Analyze different temperature ranges
    temp_ranges = [
        (300, 77.0, "Room temp to LN₂"),
        (77.0, 20.0, "LN₂ to liquid Ne"),
        (20.0, 4.2, "Liquid Ne to liquid He"),
        (300, 4.2, "Full range")
    ]
    
    print(f"Material: Aluminum 6061-T6")
    print(f"Geometry: {rod.description()}")
    print()
    print("Temperature Range Analysis:")
    print("Range (K)        | ΔT (K) | Power (W) | Conductance (W/K)")
    print("-" * 60)
    
    for t_hot, t_cold, desc in temp_ranges:
        delta_t = t_hot - t_cold
        power = calc.calculate_thermal_power(material, rod, t_hot, t_cold)
        conductance = calc.calculate_thermal_conductance(material, rod, t_cold, t_hot)
        print(f"{t_hot:3.0f}K → {t_cold:4.1f}K | {delta_t:6.1f} | {power:8.4f} | {conductance:11.8f}")
    
    # Example 7: Custom Geometry Application
    print("\n7. Custom Geometry Example")
    print("-" * 30)
    
    # Heat sink fin with complex cross-section
    custom_geom = create_custom(
        area_mm2=25.0,  # 25 mm² effective area
        length_mm=75,   # 75 mm length
        description="Cryogenic heat sink fin"
    )
    
    material = "copper_ofhc_rrr100"
    power = calc.calculate_thermal_power(material, custom_geom, 300.0, 77.0)
    conductance = calc.calculate_thermal_conductance(material, custom_geom, 77.0, 300.0)
    
    print(f"Application: Cryogenic Heat Sink Design")
    print(f"Material: Copper OFHC RRR=100")
    print(f"Geometry: {custom_geom.description()}")
    print(f"Temperature: 300K → 77K")
    print(f"Thermal power: {power:.3f} W")
    print(f"Thermal conductance: {conductance:.6f} W/K")
    print(f"Thermal resistance: {1/conductance:.2f} K/W")
    
    # Example 8: Design Guidelines
    print("\n8. Design Guidelines and Tips")
    print("-" * 32)
    
    print("Thermal Design Principles:")
    print("• Minimize cross-sectional area for thermal isolation")
    print("• Maximize length to increase thermal resistance")
    print("• Choose materials with appropriate thermal conductivity")
    print("• Consider temperature dependence of properties")
    print("• Account for mechanical requirements vs thermal performance")
    print()
    print("Material Selection Guidelines:")
    print("• Stainless steel: Good thermal isolation, structural strength")
    print("• Aluminum: Moderate conductivity, lightweight")
    print("• Copper: High conductivity for thermal links")
    print("• Composites (G-10): Excellent thermal isolation")
    print()
    print("Common Applications:")
    print("• Transfer lines: Minimize heat leak to cryogenic fluids")
    print("• Support structures: Balance mechanical and thermal requirements")
    print("• Thermal anchoring: Controlled heat transfer for temperature staging")
    print("• Heat exchangers: Maximize heat transfer efficiency")
    
    print("\n" + "=" * 60)
    print("✅ Thermal conductance analysis guide completed!")
    print("\nFor more information, see:")
    print("• docs/thermal_analysis.md - Detailed documentation")
    print("• examples/thermal_analysis.py - Additional examples")
    print("• CryoCalc API documentation")


if __name__ == "__main__":
    main()
