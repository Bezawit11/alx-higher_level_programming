#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 2 and len(tuple_b) == 2 or len(tuple_b) > 2:
        p = tuple_b
    if len(tuple_a) == 2 and len(tuple_b) == 1:
        p = (tuple_b[0], 0)
    if len(tuple_a) == 2 and len(tuple_b) == 0:
        p = (0, 0)
    tup = tuple((tuple_a[0] + p[0], tuple_a[1] + p[1]))
    return tup
