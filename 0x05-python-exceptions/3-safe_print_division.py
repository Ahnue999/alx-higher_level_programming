#!/usr/bin/python3


def safe_print_division(a, b):
    """
    return the quotient of a/b or None if they are not dividable
    """

    try:
        result = a/b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return (result)
