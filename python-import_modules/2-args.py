#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    c = len(args)

    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(c))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))

