#!/usr/bin/python3
''' class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py) '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' representation of a square '''

    def __init__(self, size):
        ''' instantiation of the square '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        ''' custom str method for print the rectangle '''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

    def area(self):
        ''' computes the area of the retangle '''
        return self.__size ** 2
