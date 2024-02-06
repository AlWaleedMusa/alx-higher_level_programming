#!/usr/bin/python3

""" returns the dictionary description with simple data structure """


def class_to_json(obj):
    """ Function that return the dictionary description of an obj """

    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()

    return result
