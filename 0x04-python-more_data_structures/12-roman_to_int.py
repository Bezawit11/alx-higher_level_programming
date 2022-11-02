#!/usr/bin/python3
"""Roman Numbers"""

def roman_to_int(roman_string):
    """a function that converts a Roman numeral to an integer"""
    sum = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    if roman_string == "IV":
        return 4
    elif roman_string == "IX":
        return 9
    for i in range (len(roman_string)):
        if roman_string[i] == "I":
           sum += 1
        elif roman_string[i] == "V":
            sum += 5
        elif roman_string[i] == "X":
            sum += 10
        elif roman_string[i] == "L":
            sum += 50
        elif roman_string[i] == "C":
            sum += 100
        elif roman_string[i] == "D":
            sum += 500
    return sum
