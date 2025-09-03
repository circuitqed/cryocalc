"""
CryoCalc - Cryogenic Material Property Calculator

A Python package for calculating thermal properties of materials at cryogenic temperatures (4-300K).
Converted from the original JavaScript propcalc.js implementation.

Author: CryoCalc Development Team
Version: 1.0.0
License: MIT
"""

from .properties import PropertyType, EquationType, PropertyCalculator
from .materials import MaterialDatabase
from .calculator import MaterialCalculator
from .thermal import (
    ThermalCalculator,
    Geometry,
    RodGeometry,
    TubeGeometry,
    BarGeometry,
    CustomGeometry,
    create_rod,
    create_wire,
    create_tube,
    create_bar,
    create_custom
)

__version__ = "1.0.0"
__author__ = "CryoCalc Development Team"
__email__ = "support@cryocalc.org"

# Main exports
__all__ = [
    'PropertyType',
    'EquationType', 
    'MaterialCalculator',
    'MaterialDatabase',
    'PropertyType',
    'EquationType',
    'ThermalCalculator',
    'Geometry',
    'RodGeometry',
    'TubeGeometry', 
    'BarGeometry',
    'CustomGeometry',
    'create_rod',
    'create_wire',
    'create_tube',
    'create_bar',
    'create_custom'
]
