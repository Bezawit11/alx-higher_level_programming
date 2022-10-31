#!/usr/bin/python3
"""Parent class"""

import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """eturns the list of the JSON string representation
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        from models.square import Square
        from models.rectangle import Rectangle

        if cls.__name__ == "Rectangle":
            r = Rectangle(2, 4)
        elif cls.__name__ == "Square":
            r = Square(3)
        return (r.update(**dictionary))

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
        """
        if list_objs is not None:
            k = []
            file = cls.__name__ + ".json"
            for a in list_objs:
                rep = cls.to_json_string(a.to_dictionary())
                k.append(json.loads(rep))
        with open(file, "w") as f:
            json.dump(k, f)

    @classmethod
    def load_from_file(cls):
        """returns an instance with all attributes already set
        """
        file = cls.__name__ + ".json"
        try:
            with open(file, encoding="UTF8") as f:
                m = cls.from_json_string(f.read())
        except Exception:
            return []
        k = []
        for a in m:
            s = cls.create(**a)
            k.append(s)
        return k
