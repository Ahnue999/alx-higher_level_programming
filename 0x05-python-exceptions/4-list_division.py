#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i from my_list_1 and j from my_list_2:
        try:
            new.append(i / j)
        except (ZeroDivisionError):
            new.append(0)
            print("division by 0")
        except (ValueError):
            new.append(0)
            print("wrong type")
