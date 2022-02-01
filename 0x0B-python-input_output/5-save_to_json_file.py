#!/usr/bin/python3
"""import json"""
import json


def save_to_json_file(my_obj, filename):
    """json to str"""
    with open(filename, mode="w", encoding="UTF8") as f:
        json.dump(my_obj, f)
