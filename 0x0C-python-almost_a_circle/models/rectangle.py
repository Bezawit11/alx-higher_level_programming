#!/usr/bin/python3
"""Child class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Child class of Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width value setter"""
        self.validate(value, "width")
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height value setter"""
        self.validate(value, "height")
        self.__height = value

    @property
    def x(self):
        """returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x value setter"""
        self.validate(value, "x")
        self.__x = value

    @property
    def y(self):
        """returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """y value setter"""
        self.validate(value, "y")
        self.__y = value

    @staticmethod
    def validate(ins, name):
        """validation of all setter methods and instantiation
        """
        if not isinstance(ins, int):
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if ins <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif ins < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """returns area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def to_dictionary(self):
        """returns the dictionary representation of a Square
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def __str__(self):
        """returns string representation of object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
