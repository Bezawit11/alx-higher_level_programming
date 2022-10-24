#!/usr/bin/python3
"""
    a class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    '''
        Instantiation with width and height
    '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        BaseGeometry.__init__(self, width, height)
