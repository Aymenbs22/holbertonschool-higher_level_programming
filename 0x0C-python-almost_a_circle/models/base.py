#!/usr/bin/python3
"""Class Create"""
import json


class Base:
    """New class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            iist_dictionaries = []
        return json.dumps(list_dictionaries)
