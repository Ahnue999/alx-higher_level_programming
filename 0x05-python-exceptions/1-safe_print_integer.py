#!/usr/bin/python3


def safe_print_integer(value):
    """
    prints integers, returns true if it was printed correctly
    and false other wise.
    """

    try:
        print("{:d}".format(value))
    except ValueError:
        return (False)
    return (True)
