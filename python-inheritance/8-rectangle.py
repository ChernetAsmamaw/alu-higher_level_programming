#!/usr/bin/python3
''' Integer validato: a class Rectangle that inherits from BaseGeometry (7-base_geometry.py) '''


class Rectangle(BaseGeometry):
    ''' representation of a rectangle '''

    def __init__(self, width, height):
        ''' instantiation of the rectangle '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
