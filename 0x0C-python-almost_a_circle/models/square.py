#!/usr/bin/python3
"""child class Square""" 

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
    
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.validate(value, "width")
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
