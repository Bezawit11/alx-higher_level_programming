#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    t = a_dictionary.copy()
    for a in a_dictionary:
        if a_dictionary[a] == value:
            t.pop(a)
    return t
