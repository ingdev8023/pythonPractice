"""Spiral Matrix
Given a 2D matrix, return a flat array with all of its values in clockwise order.

The returned array should have the top-left value first, move right along the top row, then down the right column, then left along the bottom row, then up the left column. Repeat inward for any remaining layers."""

def spiral_matrix(matrix):
    
    working_matrix = matrix[::]
    linear_matrix = []

    while len(working_matrix) > 1:

        #cut first row
        first_row = working_matrix[0]
        working_matrix = working_matrix[1:]
        
        
        #cut the last row
        last_row = working_matrix[len(working_matrix) - 1][::-1]
        working_matrix = working_matrix[:len(working_matrix) - 1]   

        #working on the columns

        last_column = []
        first_column = []       
        
        for i in range(len(working_matrix)):
            if len(working_matrix[i]) > 1:
                last_column.append(working_matrix[i][-1])
                working_matrix[i] = working_matrix[i][:- 1]
                first_column.append(working_matrix[i][0])
                working_matrix[i] = working_matrix[i][1:]
            else:
                last_column.extend(working_matrix[i])
                working_matrix[i] = working_matrix[i][:- 1]

        if len(last_column) or len(first_column):
            linear_matrix.extend(first_row) 
            linear_matrix.extend(last_column)  
            linear_matrix.extend(last_row)
            linear_matrix.extend(first_column[::-1])
        else: 
            linear_matrix.extend(first_row)
            linear_matrix.extend(last_row)

    #last_piece

    if len(working_matrix):
        linear_matrix.extend(working_matrix[0])    

    return linear_matrix

print(spiral_matrix([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]]))
print(spiral_matrix([[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]]))
print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral_matrix([[1, 2],[3, 4],    [5, 6],    [7, 8]]))
print(spiral_matrix([
    [1, 2, 3, 4, 5]
]))
print(spiral_matrix([ [1] ]))
print(spiral_matrix([[1],[2],[3],[4]]))


#AI solution

"""def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # 1) left to right across the top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # 2) top to bottom down the right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # 3) right to left across the bottom row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # 4) bottom to top up the left column
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result"""