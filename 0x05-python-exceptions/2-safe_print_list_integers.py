#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            c = c + 1
        except (ValueError, TypeError):
            if my_list[i] != '\0':
                continue
    print()
    return c
