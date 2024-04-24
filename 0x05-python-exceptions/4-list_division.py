#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    divides to each element of list 1 to its corresponding element
    in list 2, printing "wrong type", "division by 0", "out of ra-
    nge whenever suitable (replacing the result with the number 0)
    and returning a list filled with the results.
    """

    results = list()

    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            results.append(result)

    return (results)
