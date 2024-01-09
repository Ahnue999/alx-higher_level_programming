#!/usr/bin/python3
""" Writes on a file """


def append_write(filename="", text=""):
    """ Writes on a file """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
