#!/usr/bin/python3

""" pascal triangle """


def pascal_triangle(n):
    """ return a pascal triangle as a list"""

    triangle = []

    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)

    return triangle
