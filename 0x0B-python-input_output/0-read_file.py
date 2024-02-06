#!/usr/bin/python3

"""function that reads a text file"""


def read_file(filename=""):
    """ function that read a file and print it to stdout"""

    with open(filename, encoding="UTF-8") as file:
        for line in file:
            print(line, end="")
