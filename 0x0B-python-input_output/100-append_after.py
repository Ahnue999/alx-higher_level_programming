#!/usr/bin/python3
""" appendd after """


def append_after(filename="", search_string="", new_string=""):
    """ appendd after """

    with open(filename, "r", encoding="utf-8") as fp:

        lines = fp.readlines()

        new = []
        for line in lines:
            new.append(line)
            if search_string in line:
                new.append(new_string)

    with open(filename, "w", encoding='utf-8') as fp:

        fp.writelines(new)
