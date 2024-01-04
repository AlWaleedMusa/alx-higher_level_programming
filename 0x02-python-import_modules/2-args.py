#!/usr/bin/python3

import sys

if __name__ == "__main__":
    length = len(sys.argv)
    if length == 1:
        print("{} arguments.".format(length - 1))
    elif length == 2:
        print("{} argument:".format(length - 1))
    else:
        print("{} arguments:".format(length - 1))

    for i, value in enumerate(range(1, length)):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
