#!/usr/bin/python3
ddef safe_print_division(a, b):
    try:
        result = a/b
        return result
    except (ZeroDivisionError, TypeError):
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
