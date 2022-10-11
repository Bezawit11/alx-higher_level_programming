#!/usr/bin/python3
""""Square module."""


class Square:
    """defines a square class"""
    
    def __init__(self, size=0):
        """Constructor.
        
        Args: 
            size: size of a square
            
        Raises:
            ValueError: if the size is negative
            TypeError: if size is not an integer
         """
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
