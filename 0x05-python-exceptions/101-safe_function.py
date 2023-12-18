#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as err:
        print("Exception: ", err)
        return None
