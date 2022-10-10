#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            list.append(res)
        except (TypeError, ZeroDivisionError, IndexError):
            list.append(0)
        finally:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            elif my_list_2[i] == 0:
                print("division by 0")
            elif type(my_list_2[i]) != int and type(my_list_2[i]) != float:
                print("wrong type")
            elif type(my_list_1[i]) != int and type(my_list_1[i]) != float:
                print("wrong type")
    return list
