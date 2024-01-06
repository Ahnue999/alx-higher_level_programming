#!/usr/bin/python3
"""indent text
"""

def text_indentation(text):
    """indent text
    """

    if not isinstance(text, str):
        raise TypeError("text muse be a string")

    for i in range(len(text)):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
