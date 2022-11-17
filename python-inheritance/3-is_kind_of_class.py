#!/usr/bin/python3
''' returns True if the object is an instance of, instance of a class that inherited from '''


def is_kind_of_class(obj, a_class):
    ''' checks if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class '''
    return (isinstance(obj, a_class) or issubclass(type(obj), a_class))
