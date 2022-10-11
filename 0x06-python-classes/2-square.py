#!/usr/bin/python3
""""Square module."""


class Square:
    """defines a square class"""
    
    def __init__(self, size=0):
        """Constructor
        
        Args: 
            size: size of a square
        Raises:
            ValueError: if the size is negative
         """
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        try:
            self.__size = size
        except TypeError in e:
            print(e)
