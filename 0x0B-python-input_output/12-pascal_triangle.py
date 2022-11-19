#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers 
       representing the Pascal’s triangle of n
    """
    l = []
    s = []
    if n <= 0:
        return l
    else:
        for i in range(n):
            for j in range(i + 1):
                l.append(1)
            s.append(l)
            l = []
        return s
