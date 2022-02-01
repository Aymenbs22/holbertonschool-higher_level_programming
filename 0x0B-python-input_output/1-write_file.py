#!/usr/bin/python3
"""Write File"""


def write_file(filename="", text=""):
    """write in fille"""
    with open(filename, mode="w", encoding="UTF8") as f:
        return (f.write(text))
