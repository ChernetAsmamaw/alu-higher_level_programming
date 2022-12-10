#!/usr/bin/python3
'''
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
'''


def text_indentation(text):
    """Print text with two new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    xy = 0
    while xy < len(text) and text[xy] == ' ':
        xy += 1

    while xy < len(text):
        print(text[xy], end="")
        if text[xy] == "\n" or text[xy] in ".?:":
            if text[xy] in ".?:":
                print("\n")
            xy += 1
            while xy < len(text) and text[xy] == ' ':
                xy += 1
            continue
        xy += 1
