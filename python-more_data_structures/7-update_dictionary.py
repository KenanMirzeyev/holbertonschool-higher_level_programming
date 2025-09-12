#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        print("{}: {}".format(i, a_dictionary[i]))

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
