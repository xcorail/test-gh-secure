# test-pyp

A dummy Python project for testing purposes. This project includes basic Python modules, unit tests, and standard Python project structure.

## Project Structure

```
test-pyp/
├── src/
│   └── test_pyp/
│       ├── __init__.py
│       ├── calculator.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_utils.py
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md
```

## Features

- **Calculator**: A simple calculator class with basic arithmetic operations (add, subtract, multiply, divide)
- **Utils**: Utility functions including:
  - `greet(name)`: Generate greeting messages
  - `format_name(first_name, last_name)`: Format full names
  - `is_even(number)`: Check if a number is even
  - `reverse_string(text)`: Reverse a string

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=test_pyp

# Run specific test file
pytest tests/test_calculator.py
```

## Usage

```python
from test_pyp import Calculator, greet, format_name

# Using Calculator
calc = Calculator()
print(calc.add(5, 3))  # Output: 8
print(calc.divide(10, 2))  # Output: 5.0

# Using utility functions
print(greet("World"))  # Output: Hello, World!
print(format_name("John", "Doe"))  # Output: John Doe
```

## License

This is a dummy project for testing purposes.