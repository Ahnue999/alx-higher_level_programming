#!/usr/bin/python3
""" load add save """

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys


args = sys.argv
filename = "add_item.json"

save_to_json_file(args, filename)
