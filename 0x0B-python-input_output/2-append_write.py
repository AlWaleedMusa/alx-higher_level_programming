#!/usr/bin/python3

""" append to a file and return count of written chars """


def append_write(filename="", text=""):
    """ append to a file and return count of written chars """

    with open(filename, "a") as file:
        counter = 0
        for char in file:
            file.write(char)
            counter += 1
        return counter
