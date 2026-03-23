""" Matrix Border Flip

Given a matrix filled with exactly two distinct values, return a new matrix where only the border elements are inverted:

top row
bottom row
first column
last column

All inner elements must stay the same. """

def matrix_border_flip(matrix):
    new_matrix = []
    values = set()
    for i in matrix:
        for j in i:
            values.add(j)
    unique1,unique2 = values

    for i in range(len(matrix)):
        new_row = []
        if i == 0 or i == len(matrix) - 1:
            for j in range(len(matrix[i])):
                if matrix[i][j] == unique1:
                    new_row.append(unique2)
                else:
                    new_row.append(unique1)             
        else:
            for j in range(len(matrix[i])):
                if j == 0 or j == len(matrix[i]) - 1:
                    if matrix[i][j] == unique1:
                        new_row.append(unique2)
                    else:
                        new_row.append(unique1)  
                else:
                    new_row.append(matrix[i][j])

        new_matrix.append(new_row)    
    return new_matrix 

print(matrix_border_flip([
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]))



#chat approach

def matrix_border_flip(matrix):
    new_matrix = []
    values = set()

    for row in matrix:
        for val in row:
            values.add(val)

    unique1, unique2 = values

    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            is_border = (
                i == 0 or
                i == len(matrix) - 1 or
                j == 0 or
                j == len(matrix[i]) - 1
            )

            if is_border:
                if matrix[i][j] == unique1:
                    new_row.append(unique2)
                else:
                    new_row.append(unique1)
            else:
                new_row.append(matrix[i][j])

        new_matrix.append(new_row)

    return new_matrix