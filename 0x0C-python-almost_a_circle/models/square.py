#!/usr/bin/python3
""" a square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ a square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ init func """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str func """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update func """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ to dict """

        new = dict()

        attrs = ["id", "size", "x", "y"]

        for attr in attrs:
            if attr == "size":
                new[attr] = self.__dict__["_Rectangle__width"]
            else:
                if attr == "id":
                    new[attr] = self.__dict__[attr]
                else:
                    new[attr] = self.__dict__["_Rectangle__" + attr]

        return new
