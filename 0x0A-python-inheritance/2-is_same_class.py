#!/usr/bin/python3

""" function that return a True if obj is an instance on a_class"""


def is_same_class(obj, a_class):
	"""
	function that return a True if obj is an instance on a_class
	"""

	if isinstance(obj, a_class):
		return True
	return False
