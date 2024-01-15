#!/usr/bin/python3
""" a square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ a square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ init """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """ size """
        return self.width

    @size.setter
    def size(self, value):
        """ size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update func """
        if args != ():
            attrs = ["id", "width", "x", "y"]
            for i in range(len(args)):
                if attrs[i] == "id":
                    self.__dict__[attrs[i]] = args[i]
                else:
                    self.__dict__["_Rectangle__" + attrs[i]] = args[i]
                if attrs[i] == "width":
                    self.__dict__["_Rectangle__height"] = args[i]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key != "id":
                    key = "_Rectangle__" + key
                if key == "_Rectangle__size":
                    self.__dict__["_Rectangle__width"] = value
                    self.__dict__["_Rectangle__height"] = value
                else:
                    self.__dict__[key] = value

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
