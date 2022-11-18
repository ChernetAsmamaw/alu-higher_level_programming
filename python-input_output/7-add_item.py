#!/usr/bin/python3
"""adds all arguments to a Python list"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    textsaver = load_from_json_file('add_item.json')
except:
    textsaver = []

for i in range(1, len(sys.argv)):
    textsaver.append(sys.argv[i])
save_to_json_file(textsaver, "add_item.json")
