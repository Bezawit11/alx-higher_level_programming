#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary == {}:
        return
    for x in a_dictionary:
        if x == key:
            a_dictionary.pop(key)
            return a_dictionary
        return a_dictionary
