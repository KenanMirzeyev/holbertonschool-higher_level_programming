#!/usr/bin/python3
"""
A
"""


import json


def save_to_json_file(my_obj, filename):
    """
    A
    """
    with open(filename, "w") as json.file:
        json.dump(my_obj, json.file, indent=4)
