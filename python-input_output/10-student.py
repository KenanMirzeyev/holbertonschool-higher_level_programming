#!/usr/bin/python3
"""
Module 10-student
Defines a Student class with optional attribute filtering for JSON representation.
"""


class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.
        If attrs is a list of strings, only include attributes in that list.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list):
            f_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    f_dict[key] = self.__dict__[key]
            return f_dict
        return self.__dict__.copy()
