# CryoCalc - Cryogenic Material Property Calculator

A professional Python package for calculating thermal conductivity, specific heat, Young's modulus, and linear expansion for materials at cryogenic temperatures (4-300K).

## Features

- **Comprehensive Material Database**: Includes data for aluminum alloys, stainless steels, copper, composites, and other cryogenic materials
- **Multiple Property Types**: Calculate thermal conductivity, specific heat, Young's modulus, and linear expansion
- **Temperature Range Validation**: Ensures calculations are within valid temperature ranges for each material
- **Professional API**: Clean, well-documented Python interface
- **Command-Line Interface**: Easy-to-use CLI for quick calculations
- **Extensible Design**: Easy to add new materials and properties

## Installation

### From PyPI (when published)
```bash
pip install cryocalc
```

### From Source
```bash
git clone https://github.com/cryocalc/cryocalc.git
cd cryocalc
pip install -e .
```

### Development Installation
```bash
git clone https://github.com/cryocalc/cryocalc.git
cd cryocalc
pip install -e ".[dev]"
```

## Quick Start

### Python API

```python
from cryocalc import MaterialCalculator

# Initialize calculator
calc = MaterialCalculator()

# Calculate thermal conductivity of aluminum 6061-T6 at 77K
thermal_conductivity = calc.calculate_thermal_conductivity("aluminum_6061_t6", 77.0)
print(f"Thermal conductivity: {thermal_conductivity} W/m-K")

# Calculate specific heat of stainless steel 304 at 100K
specific_heat = calc.calculate_specific_heat("stainless_steel_304", 100.0)
print(f"Specific heat: {specific_heat} J/kg-K")

# Get material information
info = calc.get_material_summary("aluminum_6061_t6")
print(f"Material: {info['name']}")
print(f"Available properties: {list(info['properties'].keys())}")
```

### Command-Line Interface

```bash
# List available materials
cryocalc list-materials

# Get material information
cryocalc info aluminum_6061_t6

# Calculate thermal conductivity
cryocalc calculate aluminum_6061_t6 thermal_conductivity 77

# Calculate with property variant (for directional properties)
cryocalc calculate fiberglass_epoxy_g10 thermal_conductivity 100 --variant normal
```

## Supported Materials

### Aluminum Alloys
- Aluminum 1100 (UNS A91100)
- Aluminum 3003-F (UNS A93003)
- Aluminum 5083-O (UNS A95083)
- Aluminum 6061-T6 (UNS A96061)
- Aluminum 6063-T5 (UNS A96063)

### Stainless Steels
- Stainless Steel 304 (UNS S30400)
- Stainless Steel 316 (UNS S31600)

### Copper Alloys
- Copper OFHC (various RRR values)

### Composites and Polymers
- Fiberglass Epoxy G-10
- Teflon

### Other Materials
- Beryllium
- Invar (Fe-36Ni)
- Titanium Ti-6Al-4V

## Property Types

- **Thermal Conductivity** (W/m-K): Heat conduction capability
- **Specific Heat** (J/kg-K): Heat capacity per unit mass
- **Young's Modulus** (GPa): Elastic modulus
- **Linear Expansion** (10⁻⁵ m/m): Thermal expansion coefficient

## Temperature Ranges

Each material property is valid within specific temperature ranges, typically:
- **Minimum**: 4K (liquid helium temperature)
- **Maximum**: 300K (room temperature)

The package automatically validates temperature inputs and raises errors for out-of-range values.

## Advanced Usage

### Temperature Series Calculations

```python
# Calculate property over temperature range
data = calc.calculate_temperature_series(
    "aluminum_6061_t6", 
    "thermal_conductivity", 
    (50, 300),  # Temperature range
    num_points=100
)

# Plot results (requires matplotlib)
import matplotlib.pyplot as plt
plt.plot(data['temperature'], data['values'])
plt.xlabel('Temperature (K)')
plt.ylabel('Thermal Conductivity (W/m-K)')
plt.show()
```

### Custom Material Database

```python
from cryocalc import MaterialDatabase

# Load custom database
db = MaterialDatabase("custom_materials.json")
calc = MaterialCalculator(database=db)
```

## Data Sources

Material property correlations are based on:
- NIST Cryogenic Material Properties Database
- Published scientific literature
- Industry standards and handbooks

## Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black cryocalc/
```

### Type Checking

```bash
mypy cryocalc/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Citation

If you use CryoCalc in your research, please cite:

```
CryoCalc: A Python Package for Cryogenic Material Property Calculations
Version 1.0.0
https://github.com/cryocalc/cryocalc
```

## Support

- Documentation: https://cryocalc.readthedocs.io/
- Issues: https://github.com/cryocalc/cryocalc/issues
- Email: support@cryocalc.com
