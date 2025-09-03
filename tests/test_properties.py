"""
Tests for the properties module.
"""

import pytest
import math
from cryocalc.properties import PropertyCalculator, PropertyType, EquationType, erf


class TestPropertyCalculator:
    """Test cases for PropertyCalculator."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calculator = PropertyCalculator()
    
    def test_logarithmic_polynomial(self):
        """Test logarithmic polynomial calculation."""
        # Test with simple coefficients
        coefficients = [1.0, 2.0, 0.5]  # 1 + 2*log10(T) + 0.5*log10(T)^2
        temperature = 100.0
        
        result = self.calculator.logarithmic_polynomial(temperature, coefficients)
        
        # Manual calculation: 1 + 2*log10(100) + 0.5*log10(100)^2 = 1 + 2*2 + 0.5*4 = 7
        # Result should be 10^7
        expected = 10**7
        assert abs(result - expected) < 1e-6
    
    def test_logarithmic_polynomial_invalid_temperature(self):
        """Test logarithmic polynomial with invalid temperature."""
        coefficients = [1.0, 2.0]
        
        with pytest.raises(ValueError, match="Temperature must be positive"):
            self.calculator.logarithmic_polynomial(0, coefficients)
        
        with pytest.raises(ValueError, match="Temperature must be positive"):
            self.calculator.logarithmic_polynomial(-10, coefficients)
    
    def test_polynomial(self):
        """Test polynomial calculation."""
        # Test with simple coefficients: 1 + 2*T + 0.1*T^2
        coefficients = [1.0, 2.0, 0.1]
        temperature = 10.0
        
        result = self.calculator.polynomial(temperature, coefficients)
        
        # Manual calculation: 1 + 2*10 + 0.1*100 = 1 + 20 + 10 = 31
        expected = 31.0
        assert abs(result - expected) < 1e-6
    
    def test_polynomial_zero_temperature(self):
        """Test polynomial with zero temperature."""
        coefficients = [5.0, 2.0, 0.1]
        result = self.calculator.polynomial(0.0, coefficients)
        assert result == 5.0  # Should return constant term
    
    def test_polynomial_invalid_temperature(self):
        """Test polynomial with negative temperature."""
        coefficients = [1.0, 2.0]
        
        with pytest.raises(ValueError, match="Temperature must be non-negative"):
            self.calculator.polynomial(-10, coefficients)
    
    def test_rational(self):
        """Test rational function calculation."""
        # Simple rational function
        numerator_coeffs = [1.0, 2.0]  # 1 + 2*sqrt(T)
        denominator_coeffs = [1.0, 1.0]  # 1 + sqrt(T)
        temperature = 4.0  # sqrt(4) = 2
        
        result = self.calculator.rational(temperature, numerator_coeffs, denominator_coeffs)
        
        # Manual calculation: (1 + 2*2) / (1 + 2) = 5/3
        # Result should be 10^(5/3)
        expected = 10**(5.0/3.0)
        assert abs(result - expected) < 1e-6
    
    def test_rational_zero_denominator(self):
        """Test rational function with zero denominator."""
        numerator_coeffs = [1.0]
        denominator_coeffs = [0.0]  # This will cause zero denominator
        
        with pytest.raises(ValueError, match="Denominator is zero"):
            self.calculator.rational(1.0, numerator_coeffs, denominator_coeffs)
    
    def test_validate_temperature_range(self):
        """Test temperature range validation."""
        # Valid temperature
        self.calculator.validate_temperature_range(100.0, 50.0, 200.0)
        
        # Temperature too low
        with pytest.raises(ValueError, match="outside valid range"):
            self.calculator.validate_temperature_range(30.0, 50.0, 200.0)
        
        # Temperature too high
        with pytest.raises(ValueError, match="outside valid range"):
            self.calculator.validate_temperature_range(250.0, 50.0, 200.0)
        
        # Edge cases (boundary values should be valid)
        self.calculator.validate_temperature_range(50.0, 50.0, 200.0)
        self.calculator.validate_temperature_range(200.0, 50.0, 200.0)


class TestErrorFunction:
    """Test cases for error function."""
    
    def test_erf_zero(self):
        """Test error function at zero."""
        result = erf(0.0)
        assert result == 0.0
    
    def test_erf_positive(self):
        """Test error function with positive values."""
        result = erf(1.0)
        assert 0.8 < result < 0.9  # erf(1) ≈ 0.8427
        
        result = erf(2.0)
        assert 0.99 < result < 1.0  # erf(2) ≈ 0.9953
    
    def test_erf_negative(self):
        """Test error function with negative values."""
        result = erf(-1.0)
        assert -0.9 < result < -0.8  # erf(-1) ≈ -0.8427
        
        # erf is an odd function: erf(-x) = -erf(x)
        assert abs(erf(-1.0) + erf(1.0)) < 1e-10
    
    def test_erf_symmetry(self):
        """Test error function symmetry."""
        x = 1.5
        assert abs(erf(-x) + erf(x)) < 1e-10


class TestEnums:
    """Test cases for enum classes."""
    
    def test_property_type_enum(self):
        """Test PropertyType enum."""
        assert PropertyType.THERMAL_CONDUCTIVITY.value == "thermal_conductivity"
        assert PropertyType.SPECIFIC_HEAT.value == "specific_heat"
        assert PropertyType.YOUNGS_MODULUS.value == "youngs_modulus"
        assert PropertyType.LINEAR_EXPANSION.value == "linear_expansion"
        assert PropertyType.ELECTRICAL_CONDUCTIVITY.value == "electrical_conductivity"
    
    def test_equation_type_enum(self):
        """Test EquationType enum."""
        assert EquationType.LOGARITHMIC_POLYNOMIAL.value == "log_polynomial"
        assert EquationType.POLYNOMIAL.value == "polynomial"
        assert EquationType.RATIONAL.value == "rational"
        assert EquationType.ERF_COMPOSITE.value == "erf_composite"
        assert EquationType.PIECEWISE.value == "piecewise"
