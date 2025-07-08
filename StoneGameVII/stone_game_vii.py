class Solution:
    def stoneGameVII(self, stones: list[int]) -> int:
        n = len(stones)

        prefix_sum = [0] * (n + 1)
        for k in range(n):
            prefix_sum[k+1] = prefix_sum[k] + stones[k]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                current_sub_array_sum = prefix_sum[j+1] - prefix_sum[i]

                score_if_remove_left = (current_sub_array_sum - stones[i]) - dp[i+1][j]
                score_if_remove_right = (current_sub_array_sum - stones[j]) - dp[i][j-1]

                dp[i][j] = max(score_if_remove_left, score_if_remove_right)

        return dp[0][n-1]