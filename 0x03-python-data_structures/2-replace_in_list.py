#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if i == idx and idx > 0:
            my_list[i] = element
    return my_list
