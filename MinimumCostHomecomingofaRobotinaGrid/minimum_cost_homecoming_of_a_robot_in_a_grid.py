class Solution:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        start_row, start_col = startPos
        home_row, home_col = homePos

        total_cost = 0

        # Calculate cost for row movements
        if start_row < home_row:
            # Moving down
            for r in range(start_row + 1, home_row + 1):
                total_cost += rowCosts[r]
        elif start_row > home_row:
            # Moving up
            for r in range(start_row - 1, home_row - 1, -1):
                total_cost += rowCosts[r]
        # If start_row == home_row, no row movement cost

        # Calculate cost for column movements
        if start_col < home_col:
            # Moving right
            for c in range(start_col + 1, home_col + 1):
                total_cost += colCosts[c]
        elif start_col > home_col:
            # Moving left
            for c in range(start_col - 1, home_col - 1, -1):
                total_cost += colCosts[c]
        # If start_col == home_col, no column movement cost
                
        return total_cost