#!/usr/bin/python3

import sys

length = len(sys.argv)
if length < 1:
    print("0 arguments.")
else:
    print("{} arguments: ".format(length - 1))

for i, value in enumerate(range(1, length)):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
