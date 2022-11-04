#!/usr/bin/python3
# Returns a key with the biggest integer value
# If no score is found it returns None


def best_score(a_dictionary):
    return (max(a_dictionary, key=a_dictionary.get))
