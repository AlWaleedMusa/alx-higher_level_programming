#!/usr/bin/python3

"""a base class"""


class BaseGeometry():
    """ a class that raise an exception are error"""

    def area(self):
        """ raise an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        validate if input is a positive integer

        Args:
            name (str): name of the input
            value (int): value of the input

        Return:
            nothing

        Rise:
            TypeError: if value is not an int
            ValueError: if value is less than or equal to 0
        """
        try:
            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
        except Exception as e:
            return e


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        super().__init__()

        try:
            self.integer_validator("width", width)
            self._width = width
            self.integer_validator("height", height)
            self._height = height
        except (TypeError, ValueError) as e:
            print(e)
