#!/usr/bin/python3
"""Defines an addition function."""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.
    
    if the args are floats then we typecast them to ints
    
    Raises:
        TypeError: If a or b is a non-integer or a non-float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
