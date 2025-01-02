def maxProduct(nums):
        max2=0
        max1=max(nums)
        max_index = nums.index(max1)
        for index, i in enumerate(nums):  
            if i > max2 and index != max_index:
                max2 = i
        return ((max1-1)*(max2-1)) 
  
    


arr = [1, 7, 3, 4, 9, 5] 
maxProduct(arr) # Output: 63 (9*7)