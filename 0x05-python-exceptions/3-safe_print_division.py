#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("inside result: {}".format(result))
    except:
        print("inside result: {}".format(None))
        return None
    return result
