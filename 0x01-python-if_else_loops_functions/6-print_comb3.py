#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 9):
        print("{}{}".format(i), end=", " if int(str(i) + str(j)) < 89 else "\n")
