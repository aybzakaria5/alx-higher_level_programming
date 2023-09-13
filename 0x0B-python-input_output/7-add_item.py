#!/usr/bin/python3
"""the module adds all the args to a list
and saves them to a file
"""


from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    a_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    a_list = []

for arg in range(1, len(argv)):
    a_list.append(argv[arg])
save_to_json_file(a_list, "add_item.json")
