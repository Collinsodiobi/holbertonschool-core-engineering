#!/usr/bin/env python3
"""Square module that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __str__(self):
        """Return square description."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
