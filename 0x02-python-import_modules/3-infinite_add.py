#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    sum = 0
    if n == 1:
        print("{}".format(0))
    else:
        for i in range(1, len(argv)):
            sum = sum + int(argv[i])  
        print("{}".format(sum))
