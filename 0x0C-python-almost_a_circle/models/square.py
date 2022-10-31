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

    def update(self, *args, **kwargs):
        """ assigns attributes
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """returns the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
