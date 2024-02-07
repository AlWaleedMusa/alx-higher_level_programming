#!/usr/bin/python3

""" inserts a line of text to a file, after each line containing a specific string """


def append_after(filename="", search_string="", new_string=""):
	""" inserts a line of text to a file, after each line containing a specific string """

	new_list = []
	with open(filename, "r") as file:
		data = file.readlines()

		for line in data:
			new_list.append(line)
			if search_string in line:
				new_list.append(new_string)

	with open(filename, "w") as file:
		file.writelines(new_list)
