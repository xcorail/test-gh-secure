"""
Unit tests for utility functions.
"""

import pytest
from test_pyp.utils import greet, format_name, is_even, reverse_string


class TestGreet:
    """Test cases for greet function."""

    def test_greet_basic(self):
        """Test basic greeting."""
        assert greet("Alice") == "Hello, Alice!"
        assert greet("Bob") == "Hello, Bob!"

    def test_greet_empty(self):
        """Test greeting with empty string."""
        assert greet("") == "Hello, !"


class TestFormatName:
    """Test cases for format_name function."""

    def test_format_name_basic(self):
        """Test basic name formatting."""
        assert format_name("John", "Doe") == "John Doe"
        assert format_name("Jane", "Smith") == "Jane Smith"

    def test_format_name_empty(self):
        """Test name formatting with empty strings."""
        assert format_name("", "") == ""
        assert format_name("John", "") == "John"
        assert format_name("", "Doe") == "Doe"


class TestIsEven:
    """Test cases for is_even function."""

    def test_is_even_true(self):
        """Test even numbers."""
        assert is_even(2) is True
        assert is_even(0) is True
        assert is_even(-4) is True

    def test_is_even_false(self):
        """Test odd numbers."""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(-5) is False


class TestReverseString:
    """Test cases for reverse_string function."""

    def test_reverse_basic(self):
        """Test basic string reversal."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("Python") == "nohtyP"

    def test_reverse_empty(self):
        """Test empty string."""
        assert reverse_string("") == ""

    def test_reverse_palindrome(self):
        """Test palindrome."""
        assert reverse_string("racecar") == "racecar"
