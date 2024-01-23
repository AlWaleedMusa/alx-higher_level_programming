#!/usr/bin/python3
""" Creates a class Square
"""


class Square:
    """ Empty class with size attribute
    """
    def __init__(self, size=0):
        """
            Instantiation with size

        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ return current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """print square to stdout
        """
        if self.__size == 0:
            print()
        else:
            print("#" * self.__size)
