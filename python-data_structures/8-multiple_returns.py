#!/usr/bin/python3
# Returns a tuple with the length of a string and its first character
# If the sentence is empty, the 1st character should equal None


def multiple_returns(sentence):
    if sentence == '':
        return (0, None)
    return (len(sentence), sentence[0])
