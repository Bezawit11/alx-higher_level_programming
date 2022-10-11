#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square class"""
    def __init__(self, size=0):
        """Constructor.
        Args:
            size: size of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size is negative.
        """
        self.__size = size
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """Area of a square.
        Returns:
            the area.
        """
        return self.__size * self.__size
