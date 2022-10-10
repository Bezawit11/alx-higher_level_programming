#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None 
    finally:
        if result != None
            print("inside result: {:.1f}".format(result))
        else:
            print(result)
    return result
