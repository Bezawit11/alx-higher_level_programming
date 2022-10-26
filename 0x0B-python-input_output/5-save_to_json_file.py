#!/usr/bin/python3
""" save JSON to file"""

import json


def save_to_json_file(my_obj, filename):
    """
      a function that writes an Object to a text
      file, using a JSON representation:
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(json.dump(my_obj))
