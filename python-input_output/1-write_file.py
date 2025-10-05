#!/usr/bin/python3
"""
writes a string to a string
"""


def write_file(filename="", text=""):
    """
    write_file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
