#!/usr/bin/python3
"""pascal triangle"""


def factorial(n):
    """Calculate factorial
    """
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def pascal_triangle(n):
    """returns a list of lists of integers
       representing the Pascal’s triangle of n
    """
    a = []
    s = []
    if n <= 0:
        return a
    else:
        for i in range(n):
            for j in range(i + 1):
                x = factorial(i)
                y = factorial(i - j)
                z = factorial(j)
                a.append(int(x / (y * z)))
            s.append(a)
            a = []
        return s
