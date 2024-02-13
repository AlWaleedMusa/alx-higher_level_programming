#!/usr/bin/python3

""" class rectangle"""

from models.base import Base


class Rectangle(Base):
    """Initialize a new Rectangle.

    Args:
        width (int): width of the Rectangle.
        height (int): height of the Rectangle.
        x (int): x coordinate of the Rectangle.
        y (int): y coordinate of the Rectangle.
        id (int): identity of the Rectangle.
    Raises:
        TypeError: If width or height is not an int.
        ValueError: If of width or height <= 0.
        TypeError: If x or y is not an int.
        ValueError: If of x or y < 0.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def value_x(self):
        return self.__x
    
    @value_x.setter
    def value_x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def value_y(self):
        return self.__y
    
    @value_y.setter
    def value_y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return area of the rect"""
        return self.width * self.height
    
    def display(self):
        """ print rect using `#` """
        for _ in range(self.y):
            print("\n", end="")

        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """ assign an argument to each attribute
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if not arg:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if not value:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ make a dict out of the attributes"""
        return {
            "id" : self.id,
            "width" : self.width,
            "height" : self.height,
            "x" : self.x,
            "y" : self.y
        }
