#!/usr/bin/python3
"""
A
"""


def append_write(filename="", text=""):
    """
    A
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
