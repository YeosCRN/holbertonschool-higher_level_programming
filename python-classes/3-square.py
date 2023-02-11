#!/usr/bin/python3
"""Third"""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """Size and area"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Gets the area of the Square.

        Returns:
            Area of squre
        """
        return self.__size * self.__size
