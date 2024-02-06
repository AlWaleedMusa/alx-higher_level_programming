#!/usr/bin/python3

""" return a python struct from a json str """


import json


def from_json_string(my_str):
	""" return a python struct from a json str"""

	return json.loads(my_str)
