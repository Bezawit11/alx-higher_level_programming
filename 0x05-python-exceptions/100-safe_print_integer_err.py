#!/usr/bin/python3
import sys
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'") 
        return False
    return True
