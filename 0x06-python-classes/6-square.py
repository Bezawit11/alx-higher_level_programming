#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor.
        Args:
            size: size of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size is negative.
        """
        self.__size = size
        self.__position = position
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or type(position[0]) != int or type(position[1]) != int or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
    
    @property
    def size(self):
        """Properties for the size of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size is negative.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """setter of value to a size of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """Properties for the position of a square.
        Raises:
            TypeError: if size is not an integer.
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """setter of value to the position of a square.
        Raises:
            TypeError: if size is not an integer.
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
    
    def area(self):
        """Area of a square.
        Returns:
            the area.
        """
        return self.__size * self.__size
    
    def my_print(self):
        """Prints a square with '#' character"""
        if self.__size == 0:
            print()
        else:
            print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for z in range(self.__size):
                    print("#",end="")
                print()
