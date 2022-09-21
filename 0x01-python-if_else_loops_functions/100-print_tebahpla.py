#!/usr/bin/python3
j = 25
for i in range(13):
    print("{}".format(chr(97 + j)), end="")
    print("{}".format(chr(97 + j - 33)), end="")
    j -= 2
