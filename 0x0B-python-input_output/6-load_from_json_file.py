#!/usr/bin/python3
"""Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """
       a function that creates an
       Object from a “JSON file”:
    """
    with open(filename, "w") as f:
        return json.loads(f)
