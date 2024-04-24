#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Prints all elements of a list and returns the count of numbers printed
    """
    
    count = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()

    return (count)
