#!/usr/bin/python3
"""Append Write"""


def append_write(filename="", text=""):
    """Append"""
    with open(filename, mode="a", encoding="UTF8") as f:
        return f.write(text)
