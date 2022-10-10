#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(list_length):
        res = 'a'
        try:
            res = my_list_1[i] / my_list_2[i]
            list.append(res)
        except:
            list.append(0)
        finally:
            if i >= len(my_list_1) or i >= len(my_list_1):
                print("out of range")
            elif my_list_2[i] == 0:
                print("division by 0")
            elif  res == 'a':
                print("wrong type")
    return list
