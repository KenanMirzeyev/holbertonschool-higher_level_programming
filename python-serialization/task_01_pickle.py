#!/usr/bin/env python3
"""
A
"""

import pickle


class CustomObject:
    """
    A
    """
    def __init__(self, name, age, is_student):
        """
        A
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        A
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        A
        """
        try:
            with open(filename,"wb") as file:
                pickle.dump(self, file)

        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        A
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
