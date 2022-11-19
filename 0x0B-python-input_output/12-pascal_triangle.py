#!/usr/bin/python3
"""pascal triangle"""



def pascal_triangle(n):
    l = []
    s = []
    if n <= 0:
        return l
    else:
        for i in range(n):
            for j in range(i + 1):
                x = factorial(i)
                y = factorial(i - j)
                z = factorial(j)
                l.append(int(x / (y * z)))
            s.append(l)
            l = []
        return s
