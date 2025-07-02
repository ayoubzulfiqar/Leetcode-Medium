class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        dp = [0.0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = prefix_sum[i] / i

        for j in range(2, k + 1):
            new_dp = [0.0] * (n + 1)
            for i in range(j, n + 1):
                for p in range(j - 1, i):
                    current_sum = prefix_sum[i] - prefix_sum[p]
                    current_count = i - p
                    current_average = current_sum / current_count
                    
                    new_dp[i] = max(new_dp[i], dp[p] + current_average)
            dp = new_dp
            
        return dp[n]