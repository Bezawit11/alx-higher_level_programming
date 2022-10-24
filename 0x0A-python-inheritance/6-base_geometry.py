#!/usr/bin/python3
"""creating an empty class"""


class BaseGeometry:
    """
    an empty class BaseGeometry
    """
    pass

    def area(self):
        """
        Public instance method: def area(self): that raises an
        Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
