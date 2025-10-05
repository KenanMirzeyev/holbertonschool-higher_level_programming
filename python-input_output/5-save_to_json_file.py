#!/usr/bin/python3
"""
A
"""


import json


def save_to_json_file(my_obj, filename):
    """
    A
    """
    with open(filename, "w", encoding="utf-8") as json.file:
        json.dump(my_obj, json.file)
