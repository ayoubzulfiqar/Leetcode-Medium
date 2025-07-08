class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j] = number of ways to draw j segments using points 0 to i
        # Points are 0, 1, ..., n-1
        # So i goes from 0 to n-1
        
        # dp table size: n rows (for points 0 to n-1), k+1 columns (for 0 to k segments)
        dp = [[0] * (k + 1) for _ in range(n)]
        
        # prefix_sum_dp[i][j] = sum(dp[x][j] for x in range(i + 1))
        # This helps in calculating sum(dp[p][j-1] for p in range(i)) which is prefix_sum_dp[i-1][j-1]
        prefix_sum_dp = [[0] * (k + 1) for _ in range(n)]

        # Base case: 0 segments
        # There is 1 way to draw 0 segments (do nothing), regardless of how many points are available.
        for i in range(n):
            dp[i][0] = 1
            # Update prefix_sum_dp for j=0
            if i == 0:
                prefix_sum_dp[i][0] = dp[i][0]
            else:
                prefix_sum_dp[i][0] = (prefix_sum_dp[i-1][0] + dp[i][0]) % MOD

        # Fill DP table
        # j represents the number of segments (from 1 to k)
        for j in range(1, k + 1):
            # i represents the maximum point index considered (from 0 to n-1)
            for i in range(n):
                # Case 1: Point i is NOT an endpoint of any segment.
                # The j segments must be formed using points 0 to i-1.
                # This is dp[i-1][j]. If