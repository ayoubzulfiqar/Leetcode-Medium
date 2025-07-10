class Solution:
    def isPathWithEqualZerosAndOnes(self, grid: list[list[int]]) -> bool:
        R = len(grid)
        C = len(grid[0])

        # A path from (0,0) to (R-1, C-1) using only right and down moves
        # has a fixed length of (R-1) + (C-1) + 1 = R + C - 1 cells.
        # For the number of 0s and 1s to be equal along this path,
        # the total number of cells in the path must be an even number.
        # If (R + C - 1) is odd, it's impossible to have an equal count of 0s and 1s.
        if (R + C - 1) % 2 != 0:
            return False

        # The target difference (count_1s - count_0s) is 0.
        # The maximum possible absolute difference (all 1s or all 0s) is R + C - 1.
        # We use an offset to map negative differences to non-negative array indices.
        # The offset is chosen to be equal to the maximum possible absolute difference.
        # This ensures that the smallest difference (-(R+C-1)) maps to index 0,
        # and the largest difference (R+C-1) maps to index 2 * (R+C-1).
        max_abs_diff = R + C - 1
        offset = max_abs_diff
        
        # dp[r][c][diff_idx] will be True if there is a path from (0,0) to (r,c)
        # such that (count_1s - count_0s) equals (diff_idx - offset).
        # The size of the third dimension is 2 * max_abs_diff + 1 to cover the full range
        # from -max_abs_diff to +max_abs_diff.
        dp = [[[False] * (2 * max_abs_diff + 1) for _ in range(C)] for _ in range(R)]

        # Base case: Initialize the starting cell (0,0).
        # Calculate the initial difference for the first cell.
        initial_val = grid[0][0]
        initial_diff = 1 if initial_val == 1 else -1
        
        # Mark the corresponding state in the DP table as reachable.
        dp[0][0][initial_diff + offset] = True

        # Fill the DP table using dynamic programming.
        # Iterate through each cell in the grid.
        for r in range(R):
            for c in range(C):
                # For each possible difference that could lead to the current cell (r,c):
                for prev_diff_offset in range(2 * max_abs_diff + 1):
                    # If a path exists to (r,c) with this `prev_diff_offset`:
                    if dp[r][c][prev_diff_offset]:
                        # Try to move right to (r, c+1)
                        if c + 1 < C:
                            next_val = grid[r][c+1]
                            # Determine the change in difference for the next cell.
                            diff_change = 1 if next_val == 1 else -1
                            # Calculate the new difference offset for the cell (r, c+1).
                            new_diff_offset = prev_diff_offset + diff_change
                            
                            # Ensure the new_diff_offset is within valid array bounds.
                            if 0 <= new_diff_offset <= 2 * max_abs_diff:
                                dp[r][c+1][new_diff_offset] = True
                        
                        # Try to move down to (r+1, c)
                        if r + 1 < R:
                            next_val = grid[r+1][c]
                            # Determine the change in difference for the next cell.
                            diff_change = 1 if next_val == 1 else -1
                            # Calculate the new difference offset for the cell (r+1, c).
                            new_diff_offset = prev_diff_offset + diff_change
                            
                            # Ensure the new_diff_offset is within valid array bounds.
                            if 0 <= new_diff_offset <= 2 * max_abs_diff:
                                dp[r+1][c][new_diff_offset] = True
        
        # The final answer is whether the bottom-right cell (R-1, C-1) can be reached
        # with a difference of 0. A difference of 0 corresponds to `offset` in our DP table.
        return dp[R-1][C-1][offset]