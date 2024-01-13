#!/use/bin/python3
""" a Rectangle class """


from models.base import Base


class Rectangle(Base):
    """ a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x """
        return self.__x

    @x.setter
    def x(self, value):
        """ x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y """
        return self.__y

    @y.setter
    def y(self, value):
        """ y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area """
        return self.__height * self.__width

    def display(self):
        """ display """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print()

    def __str__(self):
        """str representation"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ update func """
        if args != ():
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                self.__dict__[attrs[i] if attrs[i] == "id" else "_Rectangle__" + attrs[i]] = args[i]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key != "id":
                    key = "_Rectangle__" + key
                self.__dict__[key] = value

    def to_dictionary(self):
        """ to dict """

        new = dict()

        attrs = ["id", "width", "height", "x", "y"]

        for attr in attrs:
            new[attr] = self.__dict__[attr if attr == "id" else "_Rectangle__" + attr]

        return new
