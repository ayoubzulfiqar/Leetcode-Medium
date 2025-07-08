class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        
        n = len(nums)
        max_pair_sum = 0
        
        for i in range(n // 2):
            current_sum = nums[i] + nums[n - 1 - i]
            if current_sum > max_pair_sum:
                max_pair_sum = current_sum
                
        return max_pair_sum