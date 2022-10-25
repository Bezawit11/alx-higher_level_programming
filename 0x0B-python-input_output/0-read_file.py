#!/usr/bin/python3
""" reads"""


def read_file(filename=""):
    """
     a function that reads a file
    """
    with open(filename, encoding="utf-8") as f:
        print(f)
