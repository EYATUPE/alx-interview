#!/usr/bin/python3
"""A script to calculate a pascal triangle for any number"""
def pascal_triangle(n):
    triangle = []
    if n > 0:
        for i in range(n):
            temp_list = [1 if j == 0 or j == i else triangle[i-1][j-1] + triangle[i-1][j] for j in range(i+1)]
            triangle.append(temp_list)
    return triangle
