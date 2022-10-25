#!/usr/bin/python3
"""ghj"""

import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    dict = load_from_json_file("add_item.json")
    dict.extend(sys.argv[1:])
    save_to_json_file(dict, "add_item.json")
