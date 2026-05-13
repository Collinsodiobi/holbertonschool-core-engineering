#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    # -------- size --------
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # -------- position --------
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) and n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    # -------- NEW: area --------
    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    # -------- printing --------
    def my_print(self):
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    # -------- string representation --------
    def __str__(self):
        if self.__size == 0:
            return ""

        lines = []
        lines.extend([""] * self.__position[1])

        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
