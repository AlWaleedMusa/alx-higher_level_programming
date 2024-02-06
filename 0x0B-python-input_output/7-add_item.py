#!/usr/bin/python3

""" adds all arguments to a Python list, and then save them to a file """


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    args = []

    for arg in sys.argv[1:]:
        args.append(arg)
    save_to_json_file(args, "add_item.json")
    load_from_json_file("add_item.json")
