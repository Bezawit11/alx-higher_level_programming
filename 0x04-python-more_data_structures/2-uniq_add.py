#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum1 = 0
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if my_list[i] == my_list[j] and j != i:
                my_list[j] = 0
        sum1 = sum1 + my_list[i]
    return sum1
