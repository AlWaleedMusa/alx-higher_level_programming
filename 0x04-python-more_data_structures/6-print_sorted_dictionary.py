#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    sorted_list = list(sorted(keys))
    for key in sorted_list:
        print("{}: {}".format(key, a_dictionary[key]))
