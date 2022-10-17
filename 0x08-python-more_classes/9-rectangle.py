#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """Defines a Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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
        self.__height = value

    def area(self):
        """Area of a rectangle.
        Returns:
            the area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of a rectangle.
        Returns:
            the perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        s = ""
        for i in range(self.__height):
            for j in range(self.__width):
                s = s + str(self.print_symbol)
            if i < self.__height - 1:
                s = s + '\n'
        return s

    def __repr__(self):
        """Return the official string representation of the Rectangle."""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Prints a message when an instance is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest Rectangle.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: rect_1 or rect_2 is not an instance of the class.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
    
    @classmethod
    def square(cls, size=0):
      """
      class method: creates a square, which is a type of rectangle
      """
      return cls(size, size)
