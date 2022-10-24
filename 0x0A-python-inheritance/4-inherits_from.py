#!/usr/bin/python3
"""a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the
specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Check if the object is an inheritance of a class
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) !=  a_class and isinstance(obj, a_class):
        return True
    return False
