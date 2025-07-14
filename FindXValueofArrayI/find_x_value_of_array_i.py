class Solution:
    def findXValue(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        result = [0] * k
        
        dp = [0] * k 

        for num in nums:
            new_dp = [0] * k
            
            current_rem_single = num % k
            new_dp[current_rem_single] += 1
            
            for prev_rem in range(k):
                count = dp[prev_rem]
                if count > 0:
                    current_rem_extended = (prev_rem * num) % k
                    new_dp[current_rem_extended] += count
            
            for rem in range(k):
                result[rem] += new_dp[rem]
            
            dp = new_dp
            
        return result