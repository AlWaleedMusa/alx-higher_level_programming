#!/usr/bin/python3

""" Return a sorted list"""


class MyList(list):
    """ a subclass the inherit from list main class"""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
