#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    res = 0
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            list.append(res)
            continue
        except:
            list.append(0)
        finally:
            if my_list_1[i] == '\0' or my_list_2[i] == '\0':
                print("out of range")
            if type(my_list_1[i]) != int and type(my_list_1[i]) != float:
                print("wrong type")
            if type(my_list_2[i]) != int and type(my_list_2[i]) != float:
                print("wrong type")
            if my_list_2[i] == 0:
                print("division by 0")
    return list
