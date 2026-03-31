""" Pascal's Triangle Row
Given an integer n, return the nth row of Pascal's triangle as an array.

In Pascal's Triangle, each row begins and ends with 1, and each interior value is the sum of the two values directly above it. """

def pascal_row(n):
    
    triangle= [[1],[1,1]]

    for i in range(3, n + 1):

        new_row = []
        
        for j in range(i):
            
            if j == 0:
                new_row.append(1)
            elif j == i - 1:
                new_row.append(1)                
            else:                
                new_row.append(triangle[i - 2][j - 1]+ triangle[i-2][j])          
                    
        triangle.append(new_row)

    return triangle[n - 1]

print(pascal_row(5))

#chat's
def pascal_row(n):
    row = [1]

    for _ in range(n - 1):
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]

    return row