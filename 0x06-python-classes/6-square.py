#!/usr/bin/python3
""" Creates a class Square
"""


class Square:
    """ Empty class with size attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """
            Instantiation with size

        Args:
            size: size of the square
            position: position of the square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """
        Returns current area of square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        size getter. Handle size errors
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """
        size setter. Set the size square
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def my_print(self):
        """
        Print a square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """
        position setter. Set the position of square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Handle position with errors
        """

        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
