# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :

# Input: nums = [1,2,3,1]
# Output: true
# Hint: Use sets

def contains_duplicate(nums):
    if (len(set(nums)))!=len(nums):
        return True



contains_duplicate([1,2,3,1])