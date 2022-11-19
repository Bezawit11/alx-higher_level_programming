#!/usr/bin/python3
"""ghj"""

import sys
import json
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    json_list = load_from_json_file(file)
except Exception:
    json_list = []

for a in sys.argv[1:]:
    json_list.append(a)

save_to_json_file(json_list, file)
