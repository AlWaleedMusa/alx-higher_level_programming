#!/usr/bin/python3

""" write to a file and return count of written chars"""


def write_file(filename="", text=""):
    """ a function that write to file and return count of char written"""

    with open(filename, "w") as file:
        counter = 0
        for char in text:
            file.write(char)
            counter += 1
        return counter
