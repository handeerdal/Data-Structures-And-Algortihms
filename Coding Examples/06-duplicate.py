# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

# Example

# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']


# Note:

# 4+3 comes from second and third elements from the main list.

# 3+4 comes from third and seventh elements from the main list.


def pair_sum(arr,num):
    returnedlist=[]
    for i in range(0,len(arr)-1):
        for j in range(1,len(arr)):
            if arr[j]+arr[i]==num:
                if (f'{arr[i]}+{arr[j]}') not in returnedlist:
                    returnedlist.append(f'{arr[i]}+{arr[j]}')
                 
    return returnedlist




print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))
# Output : ['2+5', '4+3', '3+4', '-2+9']
