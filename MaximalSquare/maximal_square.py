class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # dp[i][j] stores the side length of the largest square
        # whose bottom-right corner is at (i-1, j-1) in the original matrix.
        # We use m+1 and n+1 dimensions to handle boundary conditions easily,
        # where dp[0][...] and dp[...][0] are effectively padding with zeros.
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        max_side = 0

        # Iterate through the matrix, starting from (0,0) in the original matrix,
        # which corresponds to (1,1) in the dp table.
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the current cell in the original matrix is '1'
                if matrix[i-1][j-1] == '1':
                    # The side length of the square ending at (i-1, j-1)
                    # is 1 plus the minimum of the side lengths of squares
                    # ending at its top, left, and top-left neighbors.
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    
                    # Update the maximum side length found so far
                    max_side = max(max_side, dp[i][j])
                # If matrix[i-1][j-1] is '0', dp[i][j] remains 0 (its initial value)

        # The result is the area of the largest square, which is max_side * max_side
        return max_side * max_side