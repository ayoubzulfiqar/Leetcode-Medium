class Solution:
    def numberOfPairs(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        ans = 0
        
        # Check horizontally for pairs
        for r in range(m):
            prev_person_col = -1
            for c in range(n):
                if grid[r][c] > 0:  # If current cell contains a person
                    if prev_person_col != -1:
                        # If there was a previous person in this row (prev_person_col is not -1),
                        # then the path between (r, prev_person_col) and (r, c)
                        # must consist only of empty cells (0s). This is because if any
                        # non-empty cell (another person) existed between them,
                        # prev_person_col would have been updated to that cell's column.
                        # Thus, (r, prev_person_col) and (r, c) form a valid pair
                        # where both can see each other.
                        ans += 1
                    prev_person_col = c  # Update the last seen person's column
        
        # Check vertically for pairs
        for c in range(n):
            prev_person_row = -1
            for r in range(m):
                if grid[r][c] > 0:  # If current cell contains a person
                    if prev_person_row != -1:
                        # Similar logic applies for vertical pairs.
                        # (prev_person_row, c) and (r, c) form a valid pair.
                        ans += 1
                    prev_person_row = r  # Update the last seen person's row
                    
        return ans