#!/usr/bin/python

def remove_char_at(str, n):

    copy = str[:n] + str[n + 1:]
    return copy
