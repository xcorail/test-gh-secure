"""
Test PyP - A dummy Python package for testing purposes.
"""

__version__ = "0.1.0"

from .calculator import Calculator
from .utils import greet, format_name

__all__ = ["Calculator", "greet", "format_name"]
