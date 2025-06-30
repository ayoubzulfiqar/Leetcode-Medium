class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        # Initialize the top-left cell
        dp[0][0] = grid[0][0]

        # Initialize the first row (can only come from the left)
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # Initialize the first column (can only come from above)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                # The minimum path sum to (i, j) is grid[i][j]
                # plus the minimum of the path sums from (i-1, j) or (i, j-1)
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        # The bottom-right cell contains the minimum path sum to reach it
        return dp[m-1][n-1]