from setuptools import setup, find_packages

setup(
    name="test-pyp",
    version="0.1.0",
    description="A dummy Python project for testing",
    author="Test Author",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
)
