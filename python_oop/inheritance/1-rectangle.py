#!/usr/bin/env python3
"""Rectangle module that inherits from BaseGeometry."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
