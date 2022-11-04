#!/usr/bin/python3
# Returns a key with the biggest integer value
# If no score is found it returns None


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return (max(a_dictionary, key=a_dictionary.get))
