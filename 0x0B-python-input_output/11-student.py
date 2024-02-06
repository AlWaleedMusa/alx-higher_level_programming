#!/usr/bin/python3

""" make a student class and return json from it attributes"""


class Student():
    """ make a student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """

        object = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return object

            d_list = {}

            for i_atr in range(len(attrs)):
                for s_atr in object:
                    if attrs[i_atr] == s_atr:
                        d_list[s_atr] = object[s_atr]
            return d_list

        return object

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """

        for atr in json:
            self.__dict__[atr] = json[atr]
