#!/usr/bin/python3
"""
Module 11-student
Defines a Student cla
"""


class Student:
    """Defines"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary
        """
        if isinstance(attrs, list):
            f_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    f_dict[key] = self.__dict__[key]
            return f_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        with those from the given dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
