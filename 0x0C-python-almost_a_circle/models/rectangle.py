#!/usr/bin/python3
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
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
