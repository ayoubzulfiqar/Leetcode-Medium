import math

class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        num_set = set(nums)
        
        unique_sorted_nums = sorted(list(num_set))
        
        dp = {}
        
        max_streak_length = 1 
        
        for num in unique_sorted_nums:
            sqrt_num = math.isqrt(num)
            
            if sqrt_num * sqrt_num == num and sqrt_num in num_set:
                current_streak = dp[sqrt_num] + 1
            else:
                current_streak = 1
            
            dp[num] = current_streak
            
            max_streak_length = max(max_streak_length, current_streak)
            
        if max_streak_length < 2:
            return -1
        else:
            return max_streak_length