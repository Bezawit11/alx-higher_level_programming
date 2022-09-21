#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
                str[i] = chr(ord(str[i]) - 32)
        print("{}".format(str[i]))
        i += 1
