#!/usr/bin/python3
def weight_average(my_list=[]):
    sum1 = 0
    sum2 = 0
    mul = 1
    if my_list is None or my_list == []:
        return 0
    for i in range(len(my_list)):
        sum1 = sum1 + my_list[i][1]
        for j in range(len(my_list[0])):
            mul = mul * my_list[i][j]
        sum2 = sum2 + mul
        mul = 1
    return sum2 / sum1
