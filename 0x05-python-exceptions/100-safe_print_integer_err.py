#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception: {}".format(error))
        return False
    return True
