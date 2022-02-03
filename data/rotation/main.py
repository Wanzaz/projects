from tests import tests, test

"""
    You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

    Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

    We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

    "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
"""

# DESCTIOPTION: Given a rotated sorted list tha was roatated some uknown number of times, we need to find the minimum number of times it was rotated.

# check for each number in the list whether it is smaller than the number that comes before it 



def count_rotations_linear(nums):
    position = 1 
    
    while position < len(nums):    

        if position > 0 and nums[position] < nums[position-1]:
            return position

        position += 1
    
    return 0    

def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid >= lo and mid_number < nums[mid - 1]:
            # The middle position is the answer
            return mid
        
        elif mid_number < nums[hi]:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return 0

nums0 = test['input']['nums']
output0 = test['input']['nums']


result0 = count_rotations_linear(nums0)
result1 = count_rotations_binary(nums0)
print(result0)
print(result1)

# print(tests)

