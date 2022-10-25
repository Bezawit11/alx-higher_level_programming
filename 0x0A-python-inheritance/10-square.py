#!/usr/bin/python3
"""
    a class Rectangle that inherits from BaseGeometry
"""


class BaseGeometry:
    """
    an empty class BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialize
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Public instance method: def area(self): that raises an
        Exception with the message area() is not implemented
        """
        return self.width * self.height

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''
        Instantiation with width and height
    '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        BaseGeometry.__init__(self, width, height)
        
    def __str__(self):
        """returns the printable representation"""
        return ("[Rectangle]" + str(self.width) + "/" + str(self.height))
      
class Square(Rectangle):
    '''
        class Square that inherits from Rectangle
    '''
    def __init__(self, size):
        self.integer_validator("size", size)
        #Rectangle.__init__(self, size, size)
