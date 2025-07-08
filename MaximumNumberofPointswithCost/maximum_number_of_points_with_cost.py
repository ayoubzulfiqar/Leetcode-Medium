class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        m = len(points)
        n = len(points[0])

        dp = [0] * n
        for c in range(n):
            dp[c] = points[0][c]

        for r in range(1, m):
            current_dp = [0] * n

            max_val_left = float('-inf')
            for c in range(n):
                max_val_left = max(max_val_left, dp[c] + c)
                current_dp[c] = points[r][c] + max_val_left - c

            max_val_right = float('-inf')
            for c in range(n - 1, -1, -1):
                max_val_right = max(max_val_right, dp[c] - c)
                current_dp[c] = max(current_dp[c], points[r][c] + max_val_right + c)
            
            dp = current_dp
        
        return max(dp)