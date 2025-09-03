# Thermal Analysis Features

CryoCalc provides advanced thermal analysis capabilities for cryogenic applications, including thermal conductivity integration, thermal conductance calculations, and geometry-specific heat transfer analysis.

## Overview

The thermal analysis module (`cryocalc.thermal`) extends the basic material property calculations with:

- **Thermal Conductivity Integration**: Calculate integrals of k(T) over temperature ranges
- **Thermal Conductance**: Compute G = k_avg × A / L for specific geometries
- **Thermal Power**: Calculate heat transfer Q = G × ΔT between temperature points
- **Standard Geometries**: Support for rods, wires, tubes, bars, and custom shapes
- **Temperature Profiles**: Analyze thermal performance across temperature ranges

## Classes and Functions

### ThermalConductanceCalculator

The main class for thermal analysis calculations.

```python
from cryocalc import ThermalConductanceCalculator

calc = ThermalConductanceCalculator()
```

#### Methods

**`calculate_thermal_conductivity_integral(material_id, temp_low, temp_high, num_points=100)`**

Integrates thermal conductivity over a temperature range using numerical integration.

- **Parameters:**
  - `material_id` (str): Material identifier
  - `temp_low` (float): Lower temperature bound (K)
  - `temp_high` (float): Upper temperature bound (K)
  - `num_points` (int): Number of integration points (default: 100)
- **Returns:** float - Integral value (W·K/m·K)

**`calculate_thermal_conductance(material_id, geometry, temp_low, temp_high)`**

Calculates thermal conductance G = k_avg × A / L for a specific geometry.

- **Parameters:**
  - `material_id` (str): Material identifier
  - `geometry` (Geometry): Geometry object defining shape and dimensions
  - `temp_low` (float): Lower temperature (K)
  - `temp_high` (float): Upper temperature (K)
- **Returns:** float - Thermal conductance (W/K)

**`calculate_thermal_power(material_id, geometry, temp_hot, temp_cold)`**

Calculates thermal power Q = G × ΔT between two temperatures.

- **Parameters:**
  - `material_id` (str): Material identifier
  - `geometry` (Geometry): Geometry object
  - `temp_hot` (float): Hot side temperature (K)
  - `temp_cold` (float): Cold side temperature (K)
- **Returns:** float - Thermal power (W)

**`get_calculation_summary(material_id, geometry, temp_hot, temp_cold)`**

Provides comprehensive thermal analysis summary.

- **Returns:** dict - Complete analysis including conductance, power, resistance, and material properties

### Geometry Classes

#### Base Geometry Class

All geometry classes inherit from the base `Geometry` class:

```python
class Geometry:
    def cross_sectional_area(self) -> float:
        """Return cross-sectional area in m²"""
        
    def description(self) -> str:
        """Return human-readable description"""
```

#### RodGeometry / WireGeometry

Circular cross-section geometries. Automatically classified as "wire" if diameter < 1mm.

```python
from cryocalc import RodGeometry

rod = RodGeometry(diameter=0.010, length=0.100)  # 10mm diameter, 100mm length
```

#### TubeGeometry

Hollow circular cross-section with wall thickness.

```python
from cryocalc import TubeGeometry

tube = TubeGeometry(
    outer_diameter=0.0254,    # 25.4mm outer diameter
    wall_thickness=0.0016,    # 1.6mm wall thickness
    length=1.0                # 1000mm length
)
```

#### BarGeometry

Rectangular cross-section.

```python
from cryocalc import BarGeometry

bar = BarGeometry(
    width=0.010,      # 10mm width
    thickness=0.005,  # 5mm thickness
    length=0.100      # 100mm length
)
```

#### CustomGeometry

User-defined geometry with specified cross-sectional area.

```python
from cryocalc import CustomGeometry

custom = CustomGeometry(
    area=50e-6,              # 50 mm² = 50e-6 m²
    length=0.150,            # 150mm length
    description="Heat sink fin"
)
```

### Helper Functions

Convenience functions for creating geometries with millimeter dimensions:

```python
from cryocalc import create_rod, create_wire, create_tube, create_bar, create_custom

# Create geometries with mm dimensions
rod = create_rod(diameter_mm=10, length_mm=100)
wire = create_wire(diameter_mm=0.5, length_mm=50)
tube = create_tube(outer_diameter_mm=25.4, wall_thickness_mm=1.6, length_mm=1000)
bar = create_bar(width_mm=10, thickness_mm=5, length_mm=100)
custom = create_custom(area_mm2=50, length_mm=150, description="Custom shape")
```

## Usage Examples

### Basic Thermal Conductance Calculation

```python
from cryocalc import ThermalConductanceCalculator, create_rod

# Initialize calculator
calc = ThermalConductanceCalculator()

# Create geometry
rod = create_rod(diameter_mm=10, length_mm=100)

# Calculate thermal conductance
material = "aluminum_6061_t6"
conductance = calc.calculate_thermal_conductance(material, rod, 77, 300)
print(f"Thermal conductance: {conductance:.6f} W/K")

# Calculate thermal power
power = calc.calculate_thermal_power(material, rod, 300, 77)
print(f"Thermal power: {power:.3f} W")
```

### Material Comparison

```python
from cryocalc import ThermalConductanceCalculator, create_rod

calc = ThermalConductanceCalculator()
rod = create_rod(diameter_mm=5, length_mm=50)

materials = ["copper_ofhc_rrr100", "aluminum_6061_t6", "stainless_steel_304"]

print("Material Comparison (300K → 77K):")
print("-" * 40)
for material in materials:
    power = calc.calculate_thermal_power(material, rod, 300, 77)
    conductance = calc.calculate_thermal_conductance(material, rod, 77, 300)
    print(f"{material:20s}: {power:8.3f} W, {conductance:.6f} W/K")
```

### Geometry Comparison

```python
from cryocalc import ThermalConductanceCalculator, create_rod, create_tube, create_bar

calc = ThermalConductanceCalculator()
material = "aluminum_6061_t6"

geometries = [
    ("Rod", create_rod(diameter_mm=10, length_mm=100)),
    ("Tube", create_tube(outer_diameter_mm=12, wall_thickness_mm=1, length_mm=100)),
    ("Bar", create_bar(width_mm=10, thickness_mm=5, length_mm=100))
]

print("Geometry Comparison (300K → 77K):")
print("-" * 50)
for name, geom in geometries:
    power = calc.calculate_thermal_power(material, geom, 300, 77)
    area = geom.cross_sectional_area() * 1e6  # Convert to mm²
    print(f"{name:4s}: {area:6.1f} mm², {power:8.3f} W")
```

### Thermal Conductivity Integration

```python
from cryocalc import ThermalConductanceCalculator

calc = ThermalConductanceCalculator()
material = "copper_ofhc_rrr100"

# Calculate integrals over different temperature ranges
ranges = [(4, 77), (77, 300), (4, 300)]

print("Thermal Conductivity Integrals:")
print("-" * 40)
for t_low, t_high in ranges:
    integral = calc.calculate_thermal_conductivity_integral(material, t_low, t_high)
    avg_k = integral / (t_high - t_low)
    print(f"{t_low:3.0f}K → {t_high:3.0f}K: {integral:8.1f} W·K/m·K, avg = {avg_k:.1f} W/m·K")
```

### Comprehensive Analysis

```python
from cryocalc import ThermalConductanceCalculator, create_tube

calc = ThermalConductanceCalculator()

# Cryogenic transfer line analysis
material = "stainless_steel_304"
tube = create_tube(outer_diameter_mm=25.4, wall_thickness_mm=1.6, length_mm=1000)

summary = calc.get_calculation_summary(material, tube, 300.0, 4.2)

print("Cryogenic Transfer Line Analysis")
print("=" * 40)
print(f"Material: {summary['material_name']}")
print(f"Geometry: {summary['geometry_description']}")
print(f"Length: {summary['length']:.0f} mm")
print(f"Cross-sectional area: {summary['cross_sectional_area']:.1f} mm²")
print()
print("Temperature Analysis:")
print(f"  Hot side: {summary['temp_hot']:.1f} K")
print(f"  Cold side: {summary['temp_cold']:.1f} K")
print(f"  ΔT: {summary['delta_t']:.1f} K")
print()
print("Thermal Performance:")
print(f"  Conductance: {summary['thermal_conductance']:.6f} W/K")
print(f"  Resistance: {summary['thermal_resistance']:.1f} K/W")
print(f"  Heat leak: {summary['thermal_power']:.3f} W")
```

## Applications

### Cryogenic System Design

- **Transfer lines**: Minimize heat leak in cryogenic fluid transfer
- **Support structures**: Balance mechanical strength vs thermal conductance
- **Thermal anchoring**: Design thermal links for temperature staging
- **Heat exchangers**: Optimize geometry for heat transfer efficiency

### Material Selection

- **Thermal isolation**: Choose materials with low thermal conductivity
- **Thermal conduction**: Select high-conductivity materials for heat sinks
- **Temperature staging**: Design intermediate temperature anchors
- **Structural support**: Balance thermal and mechanical requirements

### Performance Optimization

- **Geometry optimization**: Minimize cross-sectional area, maximize length
- **Multi-material design**: Use different materials in series
- **Temperature profiling**: Understand heat transfer across temperature ranges
- **Heat load budgeting**: Calculate total system heat loads

## Temperature Considerations

All calculations respect material temperature limits:

- **Automatic validation**: Temperature ranges checked against material database
- **Cryogenic focus**: Optimized for 4K to 300K temperature range
- **Integration accuracy**: Numerical integration captures temperature dependence
- **Realistic modeling**: Accounts for strong temperature dependence of properties

## Units and Conventions

- **Temperature**: Kelvin (K)
- **Length**: Meters (m), with mm helper functions
- **Area**: Square meters (m²), displayed as mm² for convenience
- **Thermal conductivity**: W/m·K
- **Thermal conductance**: W/K
- **Thermal power**: Watts (W)
- **Thermal resistance**: K/W

## Error Handling

The thermal analysis module includes comprehensive error checking:

- **Temperature range validation**: Ensures temperatures are within material limits
- **Geometry validation**: Checks for physical validity (positive dimensions)
- **Material existence**: Verifies materials exist in database
- **Property availability**: Confirms thermal conductivity data is available
