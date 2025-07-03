def find_missing_element(nums):
    n = len(nums)
    if not nums or nums[0] != 0:
        return 0

    for i in range(n):
        if nums[i] != i:
            return i
            
    return n