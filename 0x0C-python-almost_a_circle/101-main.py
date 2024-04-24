#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(50, 10), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(25, 70, 50), Square(80, 50, 70)]

    Base.draw(list_rectangles, list_squares)
