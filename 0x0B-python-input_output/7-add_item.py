#!/usr/bin/python3

""" adds all arguments to a Python list, and then save them to a file """


import json
import sys


def main():
    """ entry point"""

    args_list = sys.argv[1:]
    save_to_json_file(args_list, "add_item.json")
    print(load_from_json_file("add_item.json"))

def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """

    with open(filename, "a") as file:
        json_str = json.dumps(my_obj)
        file.write(json_str)

def load_from_json_file(filename):
    " creates an Object from a “JSON file” "

    with open(filename) as file:
        data = file.read()
        return json.loads(data)

if __name__ == "__main__":
    main()
