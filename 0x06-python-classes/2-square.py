#!/usr/bin/python3
""" Creates a class Square
"""


class Square:
    """ Empty class with size attribute
    """
    def __init__(self, size):
        """
            Instantiation with size

        Args:
            size: size of the square
        """
        self.__size = size

        if self.__size != int:
            raise TypeError("size must be an integer")
        
        if self.__size < 0:
            raise ValueError("size must be >= 0")
