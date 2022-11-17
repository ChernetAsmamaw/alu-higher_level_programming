#!/usr/bin/python3
''' Same class or inherit from '''


def inherits_from(obj, a_class):
    ''' checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class '''
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
