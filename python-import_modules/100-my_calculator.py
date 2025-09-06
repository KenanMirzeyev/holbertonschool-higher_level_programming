#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    ope = sys.argv[2]
    b = int(sys.argv[3])

    if ope == '+':
        result = add(a, b)
    elif ope == '-':
        result = sub(a, b)
    elif ope == '*':
        result = mul(a, b)
    elif ope == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print('{} {} {} = {}'.format(a, ope, b, result))
