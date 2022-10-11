#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
        if int(size) < 0:
            raise Exception("size must be >= 0")
        try:
            self.__size = size
        except TypeError in e:
            print(e)
    def area(self):
        return self.__size * self.__size
