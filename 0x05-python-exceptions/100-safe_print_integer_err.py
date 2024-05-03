#!/usr/bin/python3


def safe_print_integer_err(value):
    """
    safe print integer with error massage
    """

    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as msg:
        print("Exception:", msg)
        return (False)
