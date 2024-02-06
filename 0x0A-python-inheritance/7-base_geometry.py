#!/usr/bin/python3

""" a class that validate integers"""


class BaseGeometry():
	""" a class that raise an exception are error"""
	def __init__(self):
		pass

	def area(self):
		""" raise an exception"""
		raise Exception("area() is not implemented")
	
	def integer_validator(self, name, value):
		""" validate if input is a positive integer"""
		if isinstance(value, int):
			pass
		else:
			raise TypeError("{} must be an integer".format(name))
		if value <= 0:
			raise ValueError("{} must be greater than 0".format(name))
