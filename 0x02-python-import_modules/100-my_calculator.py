#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    n = len(argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != "+" and argv[2] != "-" and argv[2] != "*" and argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if argv[2] == "+":
        print("{} + {} = {}".format(argv[1], argv[2], add(argv[1], b)))
    elif argv[2] == "-":
        print("{} + {} = {}".format(a, b, sub(a, b)))
    elif argv[2] == "*":
        print("{} + {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} + {} = {}".format(a, b, div(a, b)))
