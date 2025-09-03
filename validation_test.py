#!/usr/bin/env python3
"""
Validation script to compare CryoCalc Python package results 
against the original JavaScript propcalc.js implementation.
"""

import json
import random
import subprocess
import tempfile
import os
from typing import Dict, List, Tuple, Any
from cryocalc import MaterialCalculator

class JavaScriptValidator:
    """Validates Python results against JavaScript implementation."""
    
    def __init__(self, js_file_path: str):
        self.js_file_path = js_file_path
        self.calculator = MaterialCalculator()
        
    def create_js_test_script(self, material: str, property_type: str, temperature: float) -> str:
        """Create a temporary JavaScript test script."""
        js_test_code = f"""
// Load the original propcalc.js
const fs = require('fs');
const path = require('path');

// Read and execute the original JavaScript file
const jsCode = fs.readFileSync('{self.js_file_path}', 'utf8');
eval(jsCode);

// Test the calculation
try {{
    const result = calcProperty('{material}', '{property_type}', {temperature});
    console.log(JSON.stringify({{
        material: '{material}',
        property: '{property_type}',
        temperature: {temperature},
        result: result,
        success: true
    }}));
}} catch (error) {{
    console.log(JSON.stringify({{
        material: '{material}',
        property: '{property_type}',
        temperature: {temperature},
        error: error.message,
        success: false
    }}));
}}
"""
        return js_test_code
    
    def run_js_calculation(self, material: str, property_type: str, temperature: float) -> Dict[str, Any]:
        """Run calculation using the original JavaScript."""
        js_code = self.create_js_test_script(material, property_type, temperature)
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
            f.write(js_code)
            temp_js_file = f.name
        
        try:
            # Run Node.js
            result = subprocess.run(
                ['node', temp_js_file],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                return json.loads(result.stdout.strip())
            else:
                return {
                    'material': material,
                    'property': property_type,
                    'temperature': temperature,
                    'error': f"JavaScript execution failed: {result.stderr}",
                    'success': False
                }
        except subprocess.TimeoutExpired:
            return {
                'material': material,
                'property': property_type,
                'temperature': temperature,
                'error': "JavaScript execution timed out",
                'success': False
            }
        except json.JSONDecodeError as e:
            return {
                'material': material,
                'property': property_type,
                'temperature': temperature,
                'error': f"Failed to parse JavaScript output: {e}",
                'success': False
            }
        finally:
            # Clean up temporary file
            try:
                os.unlink(temp_js_file)
            except:
                pass
    
    def run_python_calculation(self, material: str, property_type: str, temperature: float) -> Dict[str, Any]:
        """Run calculation using the Python package."""
        try:
            if property_type == 'thermal_conductivity':
                result = self.calculator.calculate_thermal_conductivity(material, temperature)
            elif property_type == 'specific_heat':
                result = self.calculator.calculate_specific_heat(material, temperature)
            elif property_type == 'youngs_modulus':
                result = self.calculator.calculate_youngs_modulus(material, temperature)
            elif property_type == 'linear_expansion':
                result = self.calculator.calculate_linear_expansion(material, temperature)
            else:
                raise ValueError(f"Unknown property type: {property_type}")
            
            return {
                'material': material,
                'property': property_type,
                'temperature': temperature,
                'result': result,
                'success': True
            }
        except Exception as e:
            return {
                'material': material,
                'property': property_type,
                'temperature': temperature,
                'error': str(e),
                'success': False
            }
    
    def compare_results(self, js_result: Dict[str, Any], py_result: Dict[str, Any]) -> Dict[str, Any]:
        """Compare JavaScript and Python results."""
        comparison = {
            'material': js_result['material'],
            'property': js_result['property'],
            'temperature': js_result['temperature'],
            'js_success': js_result['success'],
            'py_success': py_result['success'],
        }
        
        if js_result['success'] and py_result['success']:
            js_val = js_result['result']
            py_val = py_result['result']
            
            # Calculate relative difference
            if abs(js_val) > 1e-10:  # Avoid division by zero
                rel_diff = abs(js_val - py_val) / abs(js_val) * 100
            else:
                rel_diff = abs(js_val - py_val) * 100
            
            comparison.update({
                'js_result': js_val,
                'py_result': py_val,
                'absolute_diff': abs(js_val - py_val),
                'relative_diff_percent': rel_diff,
                'match': rel_diff < 0.01  # Consider match if < 0.01% difference
            })
        else:
            comparison.update({
                'js_error': js_result.get('error', 'Unknown error'),
                'py_error': py_result.get('error', 'Unknown error'),
                'match': False
            })
        
        return comparison
    
    def generate_test_cases(self, num_tests: int = 50) -> List[Tuple[str, str, float]]:
        """Generate random test cases."""
        materials = self.calculator.database.get_available_materials()
        
        # Property mapping between Python and JavaScript naming
        property_mapping = {
            'thermal_conductivity': 'thermal_conductivity',
            'specific_heat': 'specific_heat',
            'youngs_modulus': 'youngs_modulus',
            'linear_expansion': 'linear_expansion'
        }
        
        test_cases = []
        
        for _ in range(num_tests):
            material = random.choice(materials)
            
            # Get available properties for this material
            try:
                material_data = self.calculator.database._materials_data[material]
                available_properties = list(material_data['properties'].keys())
            except KeyError:
                continue
            
            # Map to JavaScript property names and filter valid ones
            js_properties = []
            for prop in available_properties:
                if prop in property_mapping:
                    js_properties.append(property_mapping[prop])
                elif prop.startswith('youngs_modulus'):
                    js_properties.append('youngs_modulus')
            
            if not js_properties:
                continue
                
            property_type = random.choice(js_properties)
            
            # Get temperature range for this material/property
            try:
                if property_type == 'youngs_modulus':
                    # For Young's modulus, we need to check both variants
                    available_props = [p for p in available_properties if p.startswith('youngs_modulus')]
                    if available_props:
                        temp_prop = available_props[0]  # Use first available variant
                    else:
                        continue
                else:
                    temp_prop = property_type
                
                min_temp, max_temp = self.calculator.database.get_temperature_range(material, temp_prop)
                temperature = random.uniform(min_temp + 1, max_temp - 1)
                
                test_cases.append((material, property_type, temperature))
            except:
                continue
        
        return test_cases
    
    def run_validation(self, num_tests: int = 30) -> Dict[str, Any]:
        """Run validation tests comparing Python vs JavaScript."""
        print(f"Generating {num_tests} random test cases...")
        test_cases = self.generate_test_cases(num_tests)
        
        if not test_cases:
            return {'error': 'No valid test cases generated'}
        
        print(f"Running validation on {len(test_cases)} test cases...")
        
        results = []
        matches = 0
        total_tests = 0
        
        for i, (material, property_type, temperature) in enumerate(test_cases):
            print(f"Test {i+1}/{len(test_cases)}: {material} {property_type} @ {temperature:.1f}K")
            
            # Run both implementations
            js_result = self.run_js_calculation(material, property_type, temperature)
            py_result = self.run_python_calculation(material, property_type, temperature)
            
            # Compare results
            comparison = self.compare_results(js_result, py_result)
            results.append(comparison)
            
            if comparison.get('match', False):
                matches += 1
            total_tests += 1
            
            # Print result
            if comparison['js_success'] and comparison['py_success']:
                if comparison['match']:
                    print(f"  ✅ MATCH: JS={comparison['js_result']:.6f}, PY={comparison['py_result']:.6f}")
                else:
                    print(f"  ❌ DIFF: JS={comparison['js_result']:.6f}, PY={comparison['py_result']:.6f} ({comparison['relative_diff_percent']:.3f}%)")
            else:
                print(f"  ❌ ERROR: JS_OK={comparison['js_success']}, PY_OK={comparison['py_success']}")
        
        # Summary
        match_rate = (matches / total_tests * 100) if total_tests > 0 else 0
        
        summary = {
            'total_tests': total_tests,
            'matches': matches,
            'match_rate_percent': match_rate,
            'results': results
        }
        
        print(f"\n📊 VALIDATION SUMMARY:")
        print(f"Total tests: {total_tests}")
        print(f"Matches: {matches}")
        print(f"Match rate: {match_rate:.1f}%")
        
        return summary

def main():
    """Main validation function."""
    js_file = '/Users/dave/Library/CloudStorage/Dropbox/code/cryocalc/propcalc.js'
    
    if not os.path.exists(js_file):
        print(f"❌ JavaScript file not found: {js_file}")
        return
    
    # Check if Node.js is available
    try:
        subprocess.run(['node', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Node.js not found. Please install Node.js to run validation.")
        return
    
    print("🔍 CryoCalc Validation: Python vs JavaScript")
    print("=" * 50)
    
    validator = JavaScriptValidator(js_file)
    results = validator.run_validation(num_tests=25)
    
    if 'error' in results:
        print(f"❌ Validation failed: {results['error']}")
        return
    
    # Analyze discrepancies
    discrepancies = [r for r in results['results'] if not r.get('match', False)]
    if discrepancies:
        print(f"\n⚠️  DISCREPANCIES FOUND ({len(discrepancies)}):")
        for disc in discrepancies[:5]:  # Show first 5
            if disc['js_success'] and disc['py_success']:
                print(f"  {disc['material']} {disc['property']} @ {disc['temperature']:.1f}K:")
                print(f"    JS: {disc['js_result']:.6f}")
                print(f"    PY: {disc['py_result']:.6f}")
                print(f"    Diff: {disc['relative_diff_percent']:.3f}%")
    
    print(f"\n🎯 VALIDATION {'PASSED' if results['match_rate_percent'] >= 95 else 'NEEDS REVIEW'}")

if __name__ == '__main__':
    main()
