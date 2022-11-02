#!/usr/bin/python3
"""complex delete"""


def complex_delete(a_dictionary, value):
    """a function that deletes keys with a specific value in a dictionary"""
    t = a_dictionary.copy()
    for a in t:
        if t[a] == value:
            a_dictionary.pop(a)
    return a_dictionary
