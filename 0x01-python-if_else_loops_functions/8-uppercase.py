#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print("{}".format(chr(ord(str[i]) - 32))
            if ord(str[i]) > 96 and ord(str[i]) < 123 else str[i],
            end="" if i < abs(len(str) - 1) else "\n")
