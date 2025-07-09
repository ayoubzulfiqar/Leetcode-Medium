class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        k = sum(nums)

        if k == 0 or k == n:
            return 0

        extended_nums = nums + nums

        current_zeros = 0
        for i in range(k):
            if extended_nums[i] == 0:
                current_zeros += 1
        
        min_swaps = current_zeros

        for i in range(1, n):
            if extended_nums[i-1] == 0:
                current_zeros -= 1
            
            if extended_nums[i+k-1] == 0:
                current_zeros += 1
            
            min_swaps = min(min_swaps, current_zeros)
        
        return min_swaps