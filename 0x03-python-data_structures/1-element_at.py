#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range (len(my_list)):
        if i == idx:
            print("Element at index {} is {}".format(idx, my_list[i]))
