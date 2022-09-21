#!/usr/bin/python3
def pow(a, b):
    res = 1
    for i in range(abs(b)):
        res = res * a
    return res if b > 0 else 1 / res
