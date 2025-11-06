# Matrix Builder
# Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.

# For example, given 2 and 3, return:

# [
#   [0, 0, 0],
#   [0, 0, 0]
# ]

def build_matrix(rows, cols):
    result_matrix = []
    for i in range(rows):
        result_matrix.append([])
        for j in range(cols):
            result_matrix[i].append(0)

    return result_matrix

build_matrix(2, 3)
build_matrix(2, 3)
build_matrix(3, 2)
build_matrix(4, 3)
build_matrix(9, 1)