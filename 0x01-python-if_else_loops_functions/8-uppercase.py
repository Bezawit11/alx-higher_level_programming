#!/usr/bin/python3
def uppercase(str):
    new = list(str)
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
                new[i] = chr(ord(str[i]) - 32
        print("{}".format(new[i]))
        i += 1
