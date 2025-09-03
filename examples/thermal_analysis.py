#!/usr/bin/env python3
"""
Thermal Analysis Examples - CryoCalc Package

Demonstrates the new thermal conductance and geometry features including:
- Thermal conductivity integration
- Thermal conductance calculations
- Thermal power calculations
- Standard geometries (rod, wire, tube, bar)
- Comprehensive thermal analysis
"""

from cryocalc import (
    ThermalConductanceCalculator,
    create_rod,
    create_wire,
    create_tube,
    create_bar,
    create_custom
)

def main():
    """Run thermal analysis examples."""
    
    print("🔥 CryoCalc - Thermal Analysis Examples")
    print("=" * 50)
    
    # Initialize thermal calculator
    thermal_calc = ThermalConductanceCalculator()
    
    # Example 1: Basic thermal conductance calculation
    print("\n1. Basic Thermal Conductance Calculation")
    print("-" * 42)
    
    # Create a copper rod connecting 300K to 77K
    copper_rod = create_rod(diameter_mm=10, length_mm=100)
    material = "copper_ofhc_rrr100"
    
    conductance = thermal_calc.calculate_thermal_conductance(
        material, copper_rod, 77.0, 300.0
    )
    
    power = thermal_calc.calculate_thermal_power(
        material, copper_rod, 300.0, 77.0
    )
    
    print(f"Material: Copper OFHC RRR=100")
    print(f"Geometry: {copper_rod.description()}")
    print(f"Temperature range: 77K to 300K")
    print(f"Thermal conductance: {conductance:.4f} W/K")
    print(f"Thermal power: {power:.2f} W")
    print(f"Thermal resistance: {1/conductance:.4f} K/W")
    
    # Example 2: Compare different materials
    print("\n2. Material Comparison")
    print("-" * 21)
    
    materials = [
        ("copper_ofhc_rrr100", "Copper OFHC RRR=100"),
        ("aluminum_6061_t6", "Aluminum 6061-T6"),
        ("stainless_steel_304", "Stainless Steel 304")
    ]
    
    rod = create_rod(diameter_mm=5, length_mm=50)
    
    print(f"Geometry: {rod.description()}")
    print(f"Temperature: 300K → 77K")
    print("\nMaterial Comparison:")
    print("Material                | Power (W) | Conductance (W/K)")
    print("-" * 55)
    
    for mat_id, mat_name in materials:
        try:
            power = thermal_calc.calculate_thermal_power(mat_id, rod, 300.0, 77.0)
            conductance = thermal_calc.calculate_thermal_conductance(mat_id, rod, 77.0, 300.0)
            print(f"{mat_name:<22} | {power:>8.3f} | {conductance:>12.6f}")
        except Exception as e:
            print(f"{mat_name:<22} | Error: {str(e)}")
    
    # Example 3: Geometry comparison
    print("\n3. Geometry Comparison")
    print("-" * 22)
    
    geometries = [
        (create_rod(diameter_mm=10, length_mm=100), "Rod"),
        (create_wire(diameter_mm=1, length_mm=100), "Wire"),
        (create_tube(outer_diameter_mm=12, wall_thickness_mm=1, length_mm=100), "Tube"),
        (create_bar(width_mm=10, thickness_mm=5, length_mm=100), "Bar")
    ]
    
    material = "aluminum_6061_t6"
    
    print(f"Material: Aluminum 6061-T6")
    print(f"Temperature: 300K → 77K")
    print("\nGeometry Comparison:")
    print("Type | Description                              | Area (mm²) | Power (W)")
    print("-" * 75)
    
    for geom, geom_type in geometries:
        power = thermal_calc.calculate_thermal_power(material, geom, 300.0, 77.0)
        area_mm2 = geom.cross_sectional_area() * 1e6
        print(f"{geom_type:<4} | {geom.description():<40} | {area_mm2:>9.2f} | {power:>8.3f}")
    
    # Example 4: Thermal conductivity integral
    print("\n4. Thermal Conductivity Integration")
    print("-" * 35)
    
    material = "copper_ofhc_rrr100"
    temp_ranges = [(4, 77), (77, 300), (4, 300)]
    
    print(f"Material: Copper OFHC RRR=100")
    print("\nThermal Conductivity Integrals:")
    print("Range (K)    | Integral (W·K/m·K) | Avg k (W/m·K)")
    print("-" * 50)
    
    for t_low, t_high in temp_ranges:
        try:
            integral = thermal_calc.calculate_thermal_conductivity_integral(
                material, t_low, t_high
            )
            avg_k = integral / (t_high - t_low)
            print(f"{t_low:3d} → {t_high:3d}   | {integral:>17.1f} | {avg_k:>11.1f}")
        except Exception as e:
            print(f"{t_low:3d} → {t_high:3d}   | Error: {str(e)}")
    
    # Example 5: Comprehensive thermal analysis
    print("\n5. Comprehensive Thermal Analysis")
    print("-" * 34)
    
    # Analyze a stainless steel tube for cryogenic transfer line
    tube = create_tube(outer_diameter_mm=25.4, wall_thickness_mm=1.6, length_mm=1000)
    material = "stainless_steel_304"
    
    summary = thermal_calc.get_calculation_summary(
        material, tube, 300.0, 4.2  # Room temp to liquid helium
    )
    
    print(f"Analysis: Cryogenic Transfer Line")
    print(f"Material: {summary['material']['name']}")
    print(f"Geometry: {summary['geometry']['description']}")
    print(f"Length: {summary['geometry']['length_mm']:.0f} mm")
    print(f"Cross-sectional area: {summary['geometry']['area_mm2']:.1f} mm²")
    print()
    print(f"Temperature Analysis:")
    print(f"  Hot side: {summary['temperatures']['hot_side_K']:.1f} K")
    print(f"  Cold side: {summary['temperatures']['cold_side_K']:.1f} K")
    print(f"  ΔT: {summary['temperatures']['delta_T_K']:.1f} K")
    print()
    print(f"Thermal Conductivity:")
    print(f"  @ {summary['temperatures']['hot_side_K']:.1f}K: {summary['thermal_conductivity']['hot_side_W_per_mK']:.3f} W/m·K")
    print(f"  @ {summary['temperatures']['cold_side_K']:.1f}K: {summary['thermal_conductivity']['cold_side_W_per_mK']:.3f} W/m·K")
    print(f"  Ratio: {summary['thermal_conductivity']['ratio']:.1f}:1")
    print()
    print(f"Thermal Performance:")
    print(f"  Conductance: {summary['results']['thermal_conductance_W_per_K']:.6f} W/K")
    print(f"  Resistance: {summary['results']['thermal_resistance_K_per_W']:.1f} K/W")
    print(f"  Heat leak: {summary['results']['thermal_power_W']:.3f} W")
    print(f"  Heat flux: {summary['results']['heat_flux_W_per_m2']:.0f} W/m²")
    
    # Example 6: Temperature-dependent analysis
    print("\n6. Temperature-Dependent Analysis")
    print("-" * 33)
    
    # Compare thermal power at different temperature differences
    rod = create_rod(diameter_mm=6, length_mm=200)
    material = "aluminum_6061_t6"
    
    temp_pairs = [
        (300, 77),   # Room temp to LN2
        (77, 20),    # LN2 to 20K
        (20, 4.2),   # 20K to LHe
        (300, 4.2)   # Room temp to LHe
    ]
    
    print(f"Material: Aluminum 6061-T6")
    print(f"Geometry: {rod.description()}")
    print("\nTemperature Range Analysis:")
    print("Range (K)      | ΔT (K) | Power (W) | Conductance (W/K)")
    print("-" * 58)
    
    for t_hot, t_cold in temp_pairs:
        try:
            power = thermal_calc.calculate_thermal_power(material, rod, t_hot, t_cold)
            conductance = thermal_calc.calculate_thermal_conductance(material, rod, t_cold, t_hot)
            delta_t = t_hot - t_cold
            print(f"{t_hot:3.0f}K → {t_cold:4.1f}K | {delta_t:>6.1f} | {power:>8.4f} | {conductance:>12.8f}")
        except Exception as e:
            print(f"{t_hot:3.0f}K → {t_cold:4.1f}K | Error: {str(e)}")
    
    # Example 7: Custom geometry
    print("\n7. Custom Geometry Example")
    print("-" * 27)
    
    # Custom cross-section (e.g., complex shape)
    custom_geom = create_custom(
        area_mm2=50.0,  # 50 mm² cross-section
        length_mm=150,  # 150 mm length
        description="Custom heat sink fin"
    )
    
    material = "copper_ofhc_rrr100"
    
    power = thermal_calc.calculate_thermal_power(material, custom_geom, 300.0, 77.0)
    conductance = thermal_calc.calculate_thermal_conductance(material, custom_geom, 77.0, 300.0)
    
    print(f"Material: Copper OFHC RRR=100")
    print(f"Geometry: {custom_geom.description()}")
    print(f"Temperature: 300K → 77K")
    print(f"Thermal power: {power:.3f} W")
    print(f"Thermal conductance: {conductance:.6f} W/K")
    
    print("\n" + "=" * 50)
    print("✅ Thermal analysis examples completed!")
    print("\nKey Features Demonstrated:")
    print("• Thermal conductivity integration over temperature ranges")
    print("• Thermal conductance calculations for various geometries")
    print("• Thermal power calculations between temperature points")
    print("• Material and geometry comparisons")
    print("• Comprehensive thermal analysis summaries")
    print("• Standard geometries: rod, wire, tube, bar, custom")

if __name__ == '__main__':
    main()
