# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
# 
def singleNumber(nums):
    counter=0
    if len(nums)==1:
        return nums[0]
    else:
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i]!=nums[j]:
                    counter+=1
            if counter==len(nums)-1:
                return nums[i]  
            else:
                counter=0  


               