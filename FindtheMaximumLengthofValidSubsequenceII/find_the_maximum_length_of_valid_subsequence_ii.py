class Solution:
    def longestValidSubsequence(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        max_length = 1
        for i in range(n):
            current_num = nums[i]
            for j in range(i):
                prev_num = nums[j]
                rem = (prev_num + current_num) % k
                if rem in dp[j]:
                    length = dp[j][rem] + 1
                else:
                    length = 2
                dp[i][rem] = max(dp[i].get(rem, 0), length)
                max_length = max(max_length, dp[i][rem])
        return max_length