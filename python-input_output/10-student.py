#!/usr/bin/python3
"""
A
"""


class Student:
    """
    A
    """
    def __init__(self, first_name, last_name, age):
        """
        A
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A
        """
        if isinstance(attrs, list):
            f_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    f_dict[k] = self.__dict__[key]
            return f_dict
        return self.__dict__.copy()
