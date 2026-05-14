#!/usr/bin/env python3
"""Square module that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize square with size."""

        super().integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)
