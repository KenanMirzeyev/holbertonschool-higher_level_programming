#!/usr/bin/python3

class CountedIterator():
    def __init__(self, i):
        self.i = iter(i)
        self.c = 0

    def __next__(self):
        item = next(self.i)
        self.c += 1
        return item

    def get_count(self):
        return self.c
