class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        min_score = nums[n - 1] - nums[0]
        
        for i in range(n - 1):
            min_val = min(nums[0] + k, nums[i+1] - k)
            max_val = max(nums[i] + k, nums[n-1] - k)
            
            min_score = min(min_score, max_val - min_val)
            
        return min_score