#!/usr/bin/env python3
"""
Manual validation script to compare specific calculations between
Python package and JavaScript implementation.
"""

import math
from cryocalc import MaterialCalculator

def js_aluminum_1100_thermal_conductivity(temperature):
    """
    JavaScript implementation for Aluminum 1100 thermal conductivity.
    Based on case 0 in propcalc.js
    """
    # Coefficients from JavaScript
    a = 23.39172
    b = -148.5733
    c = 422.1917
    d = -653.6664
    e = 607.0402
    f = -346.152
    g = 118.4276
    h = -22.2781
    i = 1.770187
    
    log_temp = math.log10(temperature)
    
    num1 = (a + b * log_temp + 
            c * pow(log_temp, 2) + 
            d * pow(log_temp, 3) + 
            e * pow(log_temp, 4) + 
            f * pow(log_temp, 5) + 
            g * pow(log_temp, 6) + 
            h * pow(log_temp, 7) + 
            i * pow(log_temp, 8))
    
    return pow(10, num1)

def js_aluminum_3003f_thermal_conductivity(temperature):
    """
    JavaScript implementation for Aluminum 3003-F thermal conductivity.
    Based on case 1 in propcalc.js
    """
    # Coefficients from JavaScript
    a = 0.63736
    b = -1.1437
    c = 7.4624
    d = -12.6905
    e = 11.9165
    f = -6.18721
    g = 1.63939
    h = -0.172667
    i = 0
    
    log_temp = math.log10(temperature)
    
    num1 = (a + b * log_temp + 
            c * pow(log_temp, 2) + 
            d * pow(log_temp, 3) + 
            e * pow(log_temp, 4) + 
            f * pow(log_temp, 5) + 
            g * pow(log_temp, 6) + 
            h * pow(log_temp, 7) + 
            i * pow(log_temp, 8))
    
    return pow(10, num1)

def js_aluminum_3003f_specific_heat(temperature):
    """
    JavaScript implementation for Aluminum 3003-F specific heat.
    Based on case 101 in propcalc.js
    """
    # Coefficients from JavaScript
    a = 46.6467
    b = -314.292
    c = 866.662
    d = -1298.3
    e = 1162.27
    f = -637.795
    g = 210.351
    h = -38.3094
    i = 2.96344
    
    log_temp = math.log10(temperature)
    
    num1 = (a + b * log_temp + 
            c * pow(log_temp, 2) + 
            d * pow(log_temp, 3) + 
            e * pow(log_temp, 4) + 
            f * pow(log_temp, 5) + 
            g * pow(log_temp, 6) + 
            h * pow(log_temp, 7) + 
            i * pow(log_temp, 8))
    
    return pow(10, num1)

def compare_calculation(material, property_type, temperature, js_func, py_material_id):
    """Compare JavaScript and Python calculations."""
    calculator = MaterialCalculator()
    
    # Get JavaScript result
    js_result = js_func(temperature)
    
    # Get Python result
    if property_type == 'thermal_conductivity':
        py_result = calculator.calculate_thermal_conductivity(py_material_id, temperature)
    elif property_type == 'specific_heat':
        py_result = calculator.calculate_specific_heat(py_material_id, temperature)
    else:
        raise ValueError(f"Unsupported property: {property_type}")
    
    # Calculate difference
    abs_diff = abs(js_result - py_result)
    rel_diff = (abs_diff / abs(js_result)) * 100 if abs(js_result) > 1e-10 else abs_diff * 100
    
    print(f"\n{material} - {property_type} @ {temperature}K:")
    print(f"  JavaScript: {js_result:.6f}")
    print(f"  Python:     {py_result:.6f}")
    print(f"  Abs diff:   {abs_diff:.6f}")
    print(f"  Rel diff:   {rel_diff:.4f}%")
    print(f"  Match:      {'✅' if rel_diff < 0.01 else '❌'}")
    
    return rel_diff < 0.01

def main():
    """Run manual validation tests."""
    print("🔍 Manual Validation: Python vs JavaScript")
    print("=" * 50)
    
    test_cases = [
        # (material_name, property, temperature, js_function, py_material_id)
        ("Aluminum 1100", "thermal_conductivity", 77.0, js_aluminum_1100_thermal_conductivity, "aluminum_1100"),
        ("Aluminum 1100", "thermal_conductivity", 150.0, js_aluminum_1100_thermal_conductivity, "aluminum_1100"),
        ("Aluminum 1100", "thermal_conductivity", 300.0, js_aluminum_1100_thermal_conductivity, "aluminum_1100"),
        
        ("Aluminum 3003-F", "thermal_conductivity", 77.0, js_aluminum_3003f_thermal_conductivity, "aluminum_3003_f"),
        ("Aluminum 3003-F", "thermal_conductivity", 150.0, js_aluminum_3003f_thermal_conductivity, "aluminum_3003_f"),
        ("Aluminum 3003-F", "thermal_conductivity", 300.0, js_aluminum_3003f_thermal_conductivity, "aluminum_3003_f"),
        
        ("Aluminum 3003-F", "specific_heat", 77.0, js_aluminum_3003f_specific_heat, "aluminum_3003_f"),
        ("Aluminum 3003-F", "specific_heat", 150.0, js_aluminum_3003f_specific_heat, "aluminum_3003_f"),
        ("Aluminum 3003-F", "specific_heat", 300.0, js_aluminum_3003f_specific_heat, "aluminum_3003_f"),
    ]
    
    matches = 0
    total = len(test_cases)
    
    for material, prop, temp, js_func, py_id in test_cases:
        try:
            if compare_calculation(material, prop, temp, js_func, py_id):
                matches += 1
        except Exception as e:
            print(f"\n❌ Error testing {material} {prop} @ {temp}K: {e}")
    
    print(f"\n📊 VALIDATION SUMMARY:")
    print(f"Total tests: {total}")
    print(f"Matches: {matches}")
    print(f"Match rate: {matches/total*100:.1f}%")
    print(f"Status: {'✅ PASSED' if matches/total >= 0.95 else '❌ NEEDS REVIEW'}")

if __name__ == '__main__':
    main()
