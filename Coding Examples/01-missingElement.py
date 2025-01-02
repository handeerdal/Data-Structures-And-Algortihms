# Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100. 
# The function takes to parameter the array and the number of elements that needs to be in array. 
# For example if we want to find missing number from 1 to 6 the second parameter will be 6.

# Example

# missing_number([1, 2, 3, 4, 6], 6) # 5

#MY SOLUTION 0(n**2) complextity

def missing_number(arr, n):
    # TODO
    for i in range(1,n+1):
        if i not in arr:
            return i
        
        
#OPTIMIZED SOLUTION

def missing_number(arr, n):
    # Sum of all numbers from 1 to n
    total_sum = n * (n + 1) // 2
    
    # Sum of elements in the given array
    array_sum = sum(arr)
    
    # The missing number is the difference between the total sum and the array sum
    return total_sum - array_sum

# Example usage:
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5