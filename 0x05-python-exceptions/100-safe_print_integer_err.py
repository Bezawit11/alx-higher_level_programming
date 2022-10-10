#!/usr/bin/python3
import sys
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except Exception as error:
        sys.stderr.write("Exception: {}".format(error))
        return False
    return True
