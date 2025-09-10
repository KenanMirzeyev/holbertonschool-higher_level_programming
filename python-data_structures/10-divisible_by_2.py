#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res_l = []
    for i in my_list:
        if i % 2 == 0:
            res_l.append(True)
        else:
            res_l.append(False)
    return res_l
