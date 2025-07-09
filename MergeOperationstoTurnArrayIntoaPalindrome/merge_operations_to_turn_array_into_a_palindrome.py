def min_merge_operations_to_palindrome(nums):
    operations = 0
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] < nums[right]:
            operations += 1
            nums[left+1] += nums[left]
            left += 1
        else: # nums[left] > nums[right]
            operations += 1
            nums[right-1] += nums[right]
            right -= 1
    
    return operations