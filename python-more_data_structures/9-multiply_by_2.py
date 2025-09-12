#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        print("{}: {}".format(i, a_dictionary[i]))


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
            del a_dictionary[key]
    return a_dictionary


def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
          key = key * 2
    return a_dictionary
