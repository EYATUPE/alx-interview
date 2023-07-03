def pascal_triangle(n):
    if n <= 0:
        return []

    pascal_triangle = [[1]]

    for i in range(1, n):
        row = [1] + [pascal_triangle[i-1][j] + pascal_triangle[i-1][j-1] for j in range(1, i)] + [1]
        pascal_triangle.append(row)

    return pascal_triangle
