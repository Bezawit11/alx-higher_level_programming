#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print("{}".format(number % 10))
        return number % 10
    print("{}".format(abs(number) % 10))
    return -1 * number % 10
