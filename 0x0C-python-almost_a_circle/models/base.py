#!/usr/bin/python3

""" class base"""

import json


class Base():
	""" class Base with 1 private attribute"""

	__nb_objects = 0
	def __init__(self, id=None):
		""" assign data to id"""
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects

	@staticmethod
	def to_json_string(list_dictionaries):
		if not list_dictionaries or list_dictionaries == []:
			return "[]"
		return json.dumps(list_dictionaries)

	@classmethod
	def save_to_file(cls, list_objs):
		filename = cls.__name__ + ".json"
		with open(filename, "w") as file:
			if list_objs is None:
				file.write("[]")
			else:
				list_dict = [i.to_dictionary() for i in list_objs]
				file.write(Base.to_json_string(list_dict))

	@staticmethod
	def from_json_string(json_string):
		if not json_string:
			return []
		else:
			return json.loads(json_string)
