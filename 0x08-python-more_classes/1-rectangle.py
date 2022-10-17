#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """Defines a Rectangle class"""
    def __init__(self, width=0, height=0):
        """Constructor.
        Args:
            width: width of a rectangle.
            height: height of a rectangle.
        Raises:
            TypeError: if width is not an integer.
            ValueError: If width is negative.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Properties for the width of a rectangle.
        Raises:
            TypeError: if width is not an integer.
            ValueError: If width is negative.
        """      
        return self.__width

    @width.setter
    def width(self, value):
        """setter of value to width of a rectangle.
        Raises:
            TypeError: if width is not an integer.
            ValueError: If width is negative.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Properties for the height of a rectangle.
        Raises:
            TypeError: if height is not an integer.
            ValueError: If height is negative.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter of value to height of a rectangle.
        Raises:
            TypeError: if height is not an integer.
            ValueError: If height is negative.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
