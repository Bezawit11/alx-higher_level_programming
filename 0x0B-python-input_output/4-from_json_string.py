#!/usr/bin/python3
"""JSON rep"""


import json


def from_json_string(my_str):
    """
      a function that returns an object (Python data structure)
      represented by a JSON string:
    """
    return json.dumps(my_str)
