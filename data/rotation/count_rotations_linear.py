def count_rotations_linear(nums):
    position = 1 
    
    while position < len(nums):    

        if position > 0 and nums[position] < nums[position-1]: #check whether the number at the current position is smaller than the one before it
            return position

        position += 1
    
    return 0 
