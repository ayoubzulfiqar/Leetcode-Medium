class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        rhombus_sums = set()

        for r in range(m):
            for c in range(n):
                # Case 1: Rhombus with side length s = 0 (single cell)
                rhombus_sums.add(grid[r][c])

                # Case 2: Rhombus with side length s > 0
                # The maximum possible side length 's' for a rhombus
                # starting at (r, c) is limited by grid boundaries.
                # A rhombus of side 's' has a height of 2*s and a width of 2*s.
                # The top corner is (r, c).
                # The bottom corner is (r + 2*s, c). So r + 2*s must be < m.
                # The left corner is (r + s, c - s). So c - s must be >= 0.
                # The right corner is (r + s, c + s). So c + s must be < n.
                # The maximum 's' overall is (min(m, n) - 1) // 2.
                max_s_for_grid = (min(m, n) - 1) // 2
                
                for s in range(1, max_s_for_grid + 1):
                    # Check if the current rhombus (defined by (r, c) and s) is within bounds
                    # Top corner: (r, c)
                    # Right corner: (r + s, c + s)
                    # Bottom corner: (r + 2*s, c)
                    # Left corner: (r + s, c - s)

                    # Check if bottom corner is within grid height
                    if r + 2 * s >= m:
                        continue
                    # Check if left corner is within grid width
                    if c - s < 0:
                        continue
                    # Check if right corner is within grid width
                    if c + s >= n:
                        continue

                    current_sum = 0
                    # Add the four corner elements
                    current_sum += grid[r][c]  # Top
                    current_sum += grid[r + s][c + s]  # Right
                    current_sum += grid[r + 2 * s][c]  # Bottom
                    current_sum += grid[r + s][c - s]  # Left

                    # Add elements along the four sides (excluding corners, which are already added)
                    # Iterate 'k' from 1 to s-1 for points between corners
                    for k in range(1, s):
                        current_sum += grid[r + k][c + k]  # Top-Right segment
                        current_sum += grid[r + s + k][c + s - k]  # Right-Bottom segment
                        current_sum += grid[r + 2 * s - k][c - k]  # Bottom-Left segment
                        current_sum += grid[r + s - k][c - s + k]  # Left-Top segment
                    
                    rhombus_sums.add(current_sum)

        # Convert set to list, sort in descending order, and return the top 3 distinct sums
        result = sorted(list(rhombus_sums), reverse=True)
        return result[:3]