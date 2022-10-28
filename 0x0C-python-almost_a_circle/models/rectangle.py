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
        self.__width = value
    @property
    def height(self):
        """returns height"""
        return self.__height
    @height.setter
    def height(self, value):
        """height value setter"""
        self.__height = value
    @property
    def x(self):
        """returns x"""
        return self.__x
    @x.setter
    def x(self, value):
        """x value setter"""
        self.__x = value
    @property
    def y(self):
        """returns y"""
        return self.__y
    @y.setter
    def y(self, value):
        """y value setter"""
        self.__y = value
        
    @staticmethod
    def validate(ins, name):
        """
          validation of all setter methods and instantiation
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
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()
            
    def to_dictionary(self):
        """returns the dictionary representation of a Square
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
    
     def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"    
