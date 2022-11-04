#!/usr/bin/python3
# Converts a Roman numeral to an integer
# If the roman_string is not a string or None, return 0


def roman_to_int(roman_string):
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not isinstance(roman_string, str)or roman_string is None:
        return 0
    pre, sum = 0, 0

    for i in roman_string:
        sum += numbers[i] if numbers[i] <= pre else numbers[i] numbers[i] - pre * 2
        pre = numbers[i]
    return sum
