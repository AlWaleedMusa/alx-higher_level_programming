#!/usr/bin/python3

""" class base"""

import json
import os


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

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)

        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + ".json"
        if not os.path.exists(file_name):
            return []
        with open(file_name,  encoding="utf-8") as file:
            n = cls.from_json_string(file.read())
            return [cls.create(**i) for i in n]
