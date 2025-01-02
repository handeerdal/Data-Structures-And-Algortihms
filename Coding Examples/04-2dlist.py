# Given 2D list calculate the sum of diagonal elements.

# Example

# myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
# diagonal_sum(myList2D) # 15


def diagonal_sum(matrix):
    total=0
    for i in range(0,len(matrix)):
        total+=matrix[i][i]
    return total

   








myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
print(diagonal_sum(myList2D))

