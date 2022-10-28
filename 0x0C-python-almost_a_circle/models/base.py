#!/usr/bin/python3
"""Parent class"""

import json


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            with open( + ".json", "w") as file:
                file.write([])
        else:
            for i in range(len(list_objs)):
                list_objs[i] = cls.to_json_string(cls.to_dictionary(self))
            with open("sample.json", "w") as file:
                file.write(list_objs)
