#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print()
        return
    else:
        for i in range(len(str)):
            print("{}".format(chr(ord(str[i]) - 32))
                  if ord(str[i]) > 96 and ord(str[i]) < 123 else str[i],
                  end="" if i < len(str) - 1 else "\n")
