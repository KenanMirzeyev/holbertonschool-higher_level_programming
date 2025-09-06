#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    add = sys.argv[1:]
    c = 0

    for ar in add:
        c += int(ar)
    print("{}".format(c))
