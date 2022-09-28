#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum1 = 0
    for i in range(len(matr)):
        for j in range(len(matr)):
            if matr[i] == matr[j] and j != i:
                matr[j] = 0
        sum1 = sum1 + matr[i]
    return sum1
