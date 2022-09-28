#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    sum = 0
    for x in a_dictionary:
        if x == key:
            sum = 1
            a_dictionary[x] = value
    if sum == 0:
        a_dictionary[key] = value
    return a_dictionary
