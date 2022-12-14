#!/usr/bin/python3
"""adding attributes"""


def add_attribute(object, name, value):
    """
        a function that adds attr
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
