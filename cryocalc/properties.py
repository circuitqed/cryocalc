"""
Property types and calculation methods for cryogenic materials.
"""

from enum import Enum
from typing import Dict, List, Tuple
import math


class PropertyType(Enum):
    """Enumeration of supported material properties."""
    THERMAL_CONDUCTIVITY = "thermal_conductivity"  # W/m-K
    SPECIFIC_HEAT = "specific_heat"  # J/kg-K
    YOUNGS_MODULUS = "youngs_modulus"  # GPa
    LINEAR_EXPANSION = "linear_expansion"  # 10^-5 m/m
    ELECTRICAL_CONDUCTIVITY = "electrical_conductivity"  # Various units


class EquationType(Enum):
    """Types of equations used for property calculations."""
    LOGARITHMIC_POLYNOMIAL = "log_polynomial"  # log10(property) = sum(a_i * log10(T)^i)
    POLYNOMIAL = "polynomial"  # property = sum(a_i * T^i)
    RATIONAL = "rational"  # Rational function form
    ERF_COMPOSITE = "erf_composite"  # Error function composite
    PIECEWISE = "piecewise"  # Piecewise functions


def erf(x: float) -> float:
    """
    Error function approximation.
    
    Args:
        x: Input value
        
    Returns:
        Approximated error function value
    """
    if x == 0:
        return 0
    
    ERF_A = 0.147
    sign = 1 if x > 0 else -1
    x = abs(x)
    
    one_plus_axsqrd = 1 + ERF_A * x * x
    four_ovr_pi_etc = 4 / math.pi + ERF_A * x * x
    ratio = four_ovr_pi_etc / one_plus_axsqrd
    ratio *= -x * x
    expofun = math.exp(ratio)
    radical = math.sqrt(1 - expofun)
    
    return radical * sign


class PropertyCalculator:
    """Base class for property calculations."""
    
    @staticmethod
    def logarithmic_polynomial(temperature: float, coefficients: List[float]) -> float:
        """
        Calculate property using logarithmic polynomial equation.
        
        log10(property) = sum(a_i * log10(T)^i)
        
        Args:
            temperature: Temperature in Kelvin
            coefficients: List of polynomial coefficients [a0, a1, a2, ...]
            
        Returns:
            Calculated property value
        """
        if temperature <= 0:
            raise ValueError("Temperature must be positive")
            
        log_temp = math.log10(temperature)
        log_result = sum(coeff * (log_temp ** i) for i, coeff in enumerate(coefficients))
        return 10 ** log_result
    
    @staticmethod
    def polynomial(temperature: float, coefficients: List[float]) -> float:
        """
        Calculate property using polynomial equation.
        
        property = sum(a_i * T^i)
        
        Args:
            temperature: Temperature in Kelvin
            coefficients: List of polynomial coefficients [a0, a1, a2, ...]
            
        Returns:
            Calculated property value
        """
        if temperature < 0:
            raise ValueError("Temperature must be non-negative")
            
        return sum(coeff * (temperature ** i) for i, coeff in enumerate(coefficients))
    
    @staticmethod
    def rational(temperature: float, numerator_coeffs: List[float], 
                denominator_coeffs: List[float]) -> float:
        """
        Calculate property using rational function.
        
        property = (sum(a_i * T^(i/2))) / (sum(b_i * T^(i/2)))
        
        Args:
            temperature: Temperature in Kelvin
            numerator_coeffs: Numerator coefficients
            denominator_coeffs: Denominator coefficients
            
        Returns:
            Calculated property value
        """
        if temperature < 0:
            raise ValueError("Temperature must be non-negative")
            
        numerator = sum(coeff * (temperature ** (i * 0.5)) 
                       for i, coeff in enumerate(numerator_coeffs))
        denominator = sum(coeff * (temperature ** (i * 0.5)) 
                         for i, coeff in enumerate(denominator_coeffs))
        
        if denominator == 0:
            raise ValueError("Denominator is zero")
            
        result = numerator / denominator
        return 10 ** result
    
    @staticmethod
    def validate_temperature_range(temperature: float, min_temp: float, max_temp: float) -> None:
        """
        Validate that temperature is within the valid range for a calculation.
        
        Args:
            temperature: Temperature to validate
            min_temp: Minimum valid temperature
            max_temp: Maximum valid temperature
            
        Raises:
            ValueError: If temperature is outside valid range
        """
        if not min_temp <= temperature <= max_temp:
            raise ValueError(
                f"Temperature {temperature}K is outside valid range "
                f"[{min_temp}K, {max_temp}K]"
            )
