#!/usr/bin/python3

"""function that reads a text file"""


def read_file(filename=""):
	""" function that read a file and print it to stdout"""

	with open(filename) as file:
		for line in file:
			print(line)
