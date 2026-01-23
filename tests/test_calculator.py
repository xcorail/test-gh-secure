"""
Unit tests for the Calculator class.
"""

import pytest
from test_pyp.calculator import Calculator


class TestCalculator:
    """Test cases for Calculator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        """Test subtraction."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(10, 10) == 0

    def test_multiply(self):
        """Test multiplication."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 100) == 0

    def test_divide(self):
        """Test division."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(9, 3) == 3
        assert self.calc.divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        """Test that dividing by zero raises an error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
