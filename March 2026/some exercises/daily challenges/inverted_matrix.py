""" Inverted Matrix
Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.
 """

def invert_matrix(matrix):
    first_value = matrix[0][0]
    second_value = matrix[0][1]
    inverted_matrix = []
    for i in matrix:
        new_row = []
        for j in i:
            if j == first_value:
                new_row.append(second_value)
            else:
                new_row.append(first_value)
        inverted_matrix.append(new_row)         
                

    return inverted_matrix

print(invert_matrix([["a", "b"], ["a", "a"]]))
print(invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]))


#chat

def invert_matrix(matrix):
    # Find the two distinct values
    values = set()
    for row in matrix:
        for val in row:
            values.add(val)

    val1, val2 = values

    inverted = []
    for row in matrix:
        new_row = []
        for val in row:
            if val == val1:
                new_row.append(val2)
            else:
                new_row.append(val1)
        inverted.append(new_row)

    return inverted
