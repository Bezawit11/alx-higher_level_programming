#!/usr/bin/python3
"""ghj"""


import json
def class_to_json(obj):
    """returns the dictionary description with simple data structure
    """
    jsonStr = json.dumps(obj.__dict__)
    return jsonStr
