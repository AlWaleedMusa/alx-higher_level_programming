#!/usr/bin/python3

""" make a student class and return json from it attributes"""


class Student():
    """ make a student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        result = {}
        if hasattr(self, "__dict__"):
            result = self.__dict__.copy()
            return result
