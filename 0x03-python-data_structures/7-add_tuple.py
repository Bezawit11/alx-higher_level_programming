#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = tuple_a
    d = tuple_b
    if len(tuple_a) == 0:
        c = (0, 0)
    if len(tuple_b) == 0:
        d = (0, 0)
    if len(tuple_a) == 1:
        c = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        d = (tuple_b[0], 0)
    tup = tuple((c[0] + d[0], c[1] + d[1]))
    return tup
