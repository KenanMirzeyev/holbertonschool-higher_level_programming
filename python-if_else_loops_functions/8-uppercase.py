#!/usr/bin/python3
def uppercase(str):
    a = ''
    for ch in str:
        if (ord('a') <= ord(ch) <= ord('z')):
            a += chr(ord(ch) - 32)
        else:
            a += ch
    print("{}".format(a))
