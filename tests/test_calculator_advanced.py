"""
Test cases for the calculator module using fixtures and parameterized tests.
"""
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator import add, subtract, multiply, divide

# Fixture for common test values
@pytest.fixture
def calculator_values():
    """Fixture providing common test values."""
    return {
        'a': 10,
        'b': 5,
        'expected_sum': 15,
        'expected_difference': 5,
        'expected_product': 50,
        'expected_quotient': 2
    }

# Basic tests using fixtures
def test_operations_with_fixture(calculator_values):
    """Test all operations using fixture values."""
    a = calculator_values['a']
    b = calculator_values['b']
    
    assert add(a, b) == calculator_values['expected_sum']
    assert subtract(a, b) == calculator_values['expected_difference']
    assert multiply(a, b) == calculator_values['expected_product']
    assert divide(a, b) == calculator_values['expected_quotient']

# Parameterized tests for addition
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 200, 300)
])
def test_add_parameterized(a, b, expected):
    """Parameterized test for the add function."""
    assert add(a, b) == expected

# Parameterized tests for subtraction
@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (2, 3, -1),
    (0, 0, 0),
    (10, 5, 5),
    (100, 50, 50)
])
def test_subtract_parameterized(a, b, expected):
    """Parameterized test for the subtract function."""
    assert subtract(a, b) == expected

# Parameterized tests for multiplication
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 5, 0),
    (10, 10, 100),
    (-5, -5, 25)
])
def test_multiply_parameterized(a, b, expected):
    """Parameterized test for the multiply function."""
    assert multiply(a, b) == expected

# Parameterized tests for division
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (5, 2, 2.5),
    (-6, 3, -2),
    (0, 5, 0),
    (10, 2, 5)
])
def test_divide_parameterized(a, b, expected):
    """Parameterized test for the divide function."""
    assert divide(a, b) == expected

# Test division by zero
def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        divide(5, 0)
