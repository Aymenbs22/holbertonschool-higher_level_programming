#!/usr/bin/python3
"""import json"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, encoding="UTF8") as f:
        return json.load(f)
