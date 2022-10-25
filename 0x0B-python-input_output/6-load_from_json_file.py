#!/usr/bin/python3
"""Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """
       a function that creates an
       Object from a “JSON file”:
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
