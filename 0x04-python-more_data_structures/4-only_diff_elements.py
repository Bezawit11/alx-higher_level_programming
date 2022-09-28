#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    h = {"hi"}
    h.remove("hi")
    sum = 0
    for x in set_1:
        for y in set_2:
            if x == y:
                sum = 1
        if sum == 0:
            h.add(x)
        sum = 0
    for x in set_2:
        for y in set_1:
            if x == y:
                sum = 1
        if sum == 0:
            h.add(x)
        sum = 0
    return h
