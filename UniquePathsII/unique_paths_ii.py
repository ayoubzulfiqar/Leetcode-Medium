class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell is an obstacle, there are no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Create a DP table to store the number of unique paths to each cell.
        # Initialize all cells to 0.
        dp = [[0] * n for _ in range(m)]

        # Base case: The starting cell has 1 way to be reached (by starting there).
        dp[0][0] = 1

        # Fill the first row:
        # A cell in the first row can only be reached from the cell to its left.
        for j in range(1, n):
            # If the current cell is not an obstacle AND the cell to its left is reachable,
            # then there's 1 way to reach this cell (from the left).
            if obstacleGrid[0][j] == 0 and dp[0][j-1] == 1:
                dp[0][j] = 1
            # If obstacleGrid[0][j] is 1 (an obstacle) or dp[0][j-1] is 0 (unreachable),
            # then dp[0][j] remains 0, meaning it's unreachable.

        # Fill the first column:
        # A cell in the first column can only be reached from the cell above it.
        for i in range(1, m):
            # If the current cell is not an obstacle AND the cell above it is reachable,
            # then there's 1 way to reach this cell (from above).
            if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1:
                dp[i][0] = 1
            # If obstacleGrid[i][0] is 1 (an obstacle) or dp[i-1][0] is 0 (unreachable),
            # then dp[i][0] remains 0, meaning it's unreachable.

        # Fill the rest of the DP table:
        # For any other cell (i, j), it can be reached either from (i-1, j) (moving down)
        # or from (i, j-1) (moving right).
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:  # If the current cell is not an obstacle
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                # If obstacleGrid[i][j] is 1 (an obstacle), dp[i][j] remains 0,
                # as no paths can go through an obstacle.

        # The result is the number of unique paths to the bottom-right corner.
        return dp[m-1][n-1]