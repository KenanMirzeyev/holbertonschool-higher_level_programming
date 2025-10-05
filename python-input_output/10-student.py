#!/usr/bin/python3
"""
tribute filtering for JSON representation.
"""


class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return
        """
        if isinstance(attrs, list):
            f_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    f_dict[key] = self.__dict__[key]
            return f_dict
        return self.__dict__.copy()
