#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        c = len(x)
        super().extend(x)
        print(f"Extended the list with [{c}] items.")

    def pop(self, index =- 1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)
