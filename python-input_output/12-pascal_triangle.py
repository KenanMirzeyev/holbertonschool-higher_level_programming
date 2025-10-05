#!/usr/bin/python3
"""
12-pascal_triangle.py
Returns a list of lists representing Pascal's Triangle of n
"""


def pascal_triangle(n):
    """Generate Pascal's triangle of n rows."""
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        row = (
            [1]
            + [prev_row[j] + prev_row[j + 1]
               for j in range(len(prev_row) - 1)]
            + [1]
        )
        triangle.append(row)

    return triangle
