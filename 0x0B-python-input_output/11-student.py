#!/usr/bin/python3
"""a class named student"""


class Student:
    """defines a students name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            d = {}
            for s in attrs:
                if s == "first_name":
                    d[s] = self.first_name
                elif s == "last_name":
                    d[s] = self.last_name
                elif s == "age":
                    d[s] = self.age
            return d
        return self.__dict__
      
    def reload_from_json(self, json):
        """Replace all attributes of the Student
        """
        for a, vb in json.items():
            setattr(self, a, b)
