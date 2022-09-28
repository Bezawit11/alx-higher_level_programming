#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    if a_dictionary is None:
        return None
    for x in a_dictionary:
        if a_dictionary[x] > a:
            a = a_dictionary[x]
            h = x
    return h
