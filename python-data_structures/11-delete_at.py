#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in range(idx):
        idx += i
        del my_list[idx]
        return my_list
