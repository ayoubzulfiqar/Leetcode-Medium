class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        
        # If the triangle has only one row, the minimum path sum is its single element.
        if n == 1:
            return triangle[0][0]
        
        # Initialize a DP array with the values of the last row of the triangle.
        # This array will store the minimum path sum from the current row's elements
        # down to the bottom.
        # We make a copy to avoid modifying the input triangle directly.
        dp = list(triangle[n - 1])

        # Iterate from the second-to-last row up to the first row (index 0).
        for r in range(n - 2, -1, -1):
            # Iterate through each element in the current row 'r'.
            # The number of elements in row 'r' is r + 1.
            for c in range(r + 1):
                # The minimum path sum to reach the bottom starting from triangle[r][c]
                # is the value of triangle[r][c] plus the minimum of the two
                # adjacent elements in the row below (which are already stored in dp).
                # These adjacent elements are dp[c] and dp[c+1] from the previous iteration
                # (which represented sums from row r+1 downwards).
                dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
        
        # After processing all rows up to the top, dp[0] will contain the minimum
        # total path sum starting from triangle[0][0] down to the bottom.
        return dp[0]