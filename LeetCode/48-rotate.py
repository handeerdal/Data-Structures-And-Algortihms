def rotate(matrix):
    n = len(matrix)  # Number of rows/columns (square matrix assumed)
    for i in range(n):
        for j in range(i + 1, n):  # Only iterate over the upper triangle
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    print(matrix)







#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
