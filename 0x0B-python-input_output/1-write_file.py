#!/usr/bin/python3
""" Writes on a file """


def write_file(filename="", text=""):
    """ Writes on a file """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
