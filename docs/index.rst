CryoCalc Documentation
======================

CryoCalc is a professional Python package for calculating thermal conductivity, specific heat, Young's modulus, and linear expansion for materials at cryogenic temperatures (4-300K).

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api
   materials
   examples
   contributing

Features
--------

* **Comprehensive Material Database**: Includes data for aluminum alloys, stainless steels, copper, composites, and other cryogenic materials
* **Multiple Property Types**: Calculate thermal conductivity, specific heat, Young's modulus, and linear expansion
* **Temperature Range Validation**: Ensures calculations are within valid temperature ranges for each material
* **Professional API**: Clean, well-documented Python interface
* **Command-Line Interface**: Easy-to-use CLI for quick calculations
* **Extensible Design**: Easy to add new materials and properties

Quick Example
-------------

.. code-block:: python

   from cryocalc import MaterialCalculator

   # Initialize calculator
   calc = MaterialCalculator()

   # Calculate thermal conductivity of aluminum 6061-T6 at 77K
   thermal_conductivity = calc.calculate_thermal_conductivity("aluminum_6061_t6", 77.0)
   print(f"Thermal conductivity: {thermal_conductivity} W/m-K")

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
