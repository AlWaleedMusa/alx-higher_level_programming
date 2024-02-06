#!/usr/bin/python3

""" a class that raise an exception are error"""


class BaseGeometry():
    """ a class that raise an exception are error"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
