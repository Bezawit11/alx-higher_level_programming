#!/usr/bin/python3
"""child class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
    
    @property
    def size(self):
        """returns size value"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """size value setter"""
        self.validate(value, "width")
        self.__size = value
        self.width = value
        self.height = value
        
    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
    
    def __str__(self):
        """returns the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
