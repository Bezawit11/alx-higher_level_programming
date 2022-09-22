#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    sum = 0
    if n == 1:
        print("{}".format(0))
    else:
        for i in range(1, len(sys.argv)):
            sum = sum + int(sys.argv[i])  
        print("{}".format(sum))
