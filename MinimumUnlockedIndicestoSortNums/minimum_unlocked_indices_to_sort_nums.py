def minimum_unlocked_indices(nums):
    n = len(nums)
    if n == 0:
        return 0
    
    sorted_nums = sorted(nums)
    
    unlocked_count = 0
    for i in range(n):
        if nums[i] != sorted_nums[i]:
            unlocked_count += 1
            
    return unlocked_count