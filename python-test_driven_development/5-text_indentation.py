#!/usr/bin/python3
'''
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
'''


def text_indentation(text):
    """prints a text with 2 new lines after each of these chars: '.' '?' ':'"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = False
    for char in text:
        if not flag:
            if char == ' ':
                continue
            else:
                flag = True
        if flag:
            if char == '.' or char == '?' or char == ':':
                print(char)
                print()
                flag = False
            else:
                print(char, end="")
