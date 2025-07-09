import math

class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # dp_prev will store the minimum costs to reach cells in the previous row
        # dp_curr will store the minimum costs to reach cells in the current row
        
        # Initialize dp_prev with the costs of the first row.
        # The cost to reach a cell in the first row is just its value.
        dp_prev = [grid[0][j] for j in range(n)]

        # Iterate from the second row (index 1) up to the last row (index m-1)
        for r in range(1, m):
            dp_curr = [0] * n  # Initialize dp values for the current row
            
            # For each cell (r, c) in the current row
            for c in range(n):
                min_cost_to_reach_current_cell = math.inf # Use math.inf for initial minimum
                
                # Consider all possible previous cells (r-1, prev_c) from which we could have moved
                for prev_c in range(n):
                    # Get the value of the cell in the previous row
                    prev_cell_value = grid[r-1][prev_c]
                    
                    # Get the minimum cost to reach this previous cell
                    cost_to_prev_cell = dp_prev[prev_c]
                    
                    # Get the cost of moving from prev_cell_value to column c in the current row
                    cost_of_move = moveCost[prev_cell_value][c]
                    
                    # Calculate the total cost to reach (r, c) via (r-1, prev_c)
                    total_cost_via_prev_cell = cost_to_prev_cell + cost_of_move
                    
                    # Update the minimum cost to reach the current cell (r, c)
                    min_cost_to_reach_current_cell = min(min_cost_to_reach_current_cell, total_cost_via_prev_cell)
                
                # The total cost for dp_curr[c] is the minimum path cost to reach this cell
                # plus the value of the current cell itself.
                dp_curr[c] = min_cost_to_reach_current_cell + grid[r][c]
            
            # After calculating all dp values for the current row,
            # set dp_prev to dp_curr for the next iteration.
            dp_prev = dp_curr
        
        # After iterating through all rows, dp_prev will contain the minimum costs
        # to reach each cell in the last row.
        # The overall minimum path cost is the minimum among these values.
        return min(dp_prev)