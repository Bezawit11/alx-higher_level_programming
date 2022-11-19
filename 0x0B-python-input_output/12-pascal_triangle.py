#!/usr/bin/python3
def pascal_triangle(n):
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
