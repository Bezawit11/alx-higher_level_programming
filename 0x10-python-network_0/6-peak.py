#!/usr/bin/python3
'''a function that finds a peak in a list of unsorted integers'''

def find_peak(list_of_integers):
    '''finds a peak'''
    if list_of_integers == [[]]:
        return None
    for i in range(len(list_of_integers)):
        a = list_of_integers[i]
        if i == 0:
            if a > list_of_integers[i + 1]:
                return list_of_integers[i]
        elif i < len(list_of_integers) - 1:
            if a > list_of_integers[i + 1] and a > list_of_integers[i - 1]:
                return a
        else:
            return a
          
