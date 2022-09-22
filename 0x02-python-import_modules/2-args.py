#!/usr/bin/python3
import sys
n = len(sys.argv)
if n == 1:
    print("{} {}".format(n - 1, "arguments."))
else:
    if n == 2:
        print("{} {}".format(n - 1, "argument:"))
    else:
        print("{} {}".format(n - 1, "arguments:"))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
