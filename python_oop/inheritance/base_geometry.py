#!/usr/bin/env python3
"""BaseGeometry module."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Calculate area (not implemented)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
