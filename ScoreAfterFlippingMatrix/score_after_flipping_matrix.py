class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Step 1: Ensure the most significant bit (first column) of each row is 1.
        # If grid[i][0] is 0, flip the entire row i.
        # This is always optimal because the leftmost bit contributes the most to the number's value.
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        
        # Step 2: For each subsequent column (from j=1 to n-1),
        # maximize the number of 1s.
        # If the count of 1s in a column is less than the count of 0s,
        # flip that column. This maximizes the contribution of that column's bit position.
        for j in range(1, n): # Start from the second column (index 1)
            count_ones = 0
            for i in range(m):
                if grid[i][j] == 1:
                    count_ones += 1
            
            # If the number of 1s is less than the number of 0s in this column,
            # flipping the column will result in more 1s.
            if count_ones < m - count_ones:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]
        
        # Step 3: Calculate the total score from the modified grid.
        total_score = 0
        for i in range(m):
            row_val = 0
            for j in range(n):
                # Calculate the value of the binary number represented by the row
                # (1 << (n - 1 - j)) gives 2 raised to the power of the bit's position value
                # e.g., for n=4, j=0 -> 2^3, j=1 -> 2^2, j=2 -> 2^1, j=3 -> 2^0
                row_val += grid[i][j] * (1 << (n - 1 - j))
            total_score += row_val
            
        return total_score