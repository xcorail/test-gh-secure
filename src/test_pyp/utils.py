"""
Utility functions for the test_pyp package.
"""


def greet(name):
    """Generate a greeting message.
    
    Args:
        name: Name of the person to greet
        
    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


def format_name(first_name, last_name):
    """Format a full name from first and last names.
    
    Args:
        first_name: First name
        last_name: Last name
        
    Returns:
        Formatted full name
    """
    return f"{first_name} {last_name}".strip()


def is_even(number):
    """Check if a number is even.
    
    Args:
        number: Number to check
        
    Returns:
        True if number is even, False otherwise
    """
    return number % 2 == 0


def reverse_string(text):
    """Reverse a string.
    
    Args:
        text: String to reverse
        
    Returns:
        Reversed string
    """
    return text[::-1]
