class Solution:
    def is_magic_square(self, subgrid: list[list[int]]) -> bool:
        nums = []
        for r in range(3):
            for c in range(3):
                val = subgrid[r][c]
                if not (1 <= val <= 9):
                    return False
                nums.append(val)
        
        if len(set(nums)) != 9:
            return False
        
        target_sum = 15

        # Check rows
        if not (sum(subgrid[0]) == target_sum and
                sum(subgrid[1]) == target_sum and
                sum(subgrid[2]) == target_sum):
            return False

        # Check columns
        if not (subgrid[0][0] + subgrid[1][0] + subgrid[2][0] == target_sum and
                subgrid[0][1] + subgrid[1][1] + subgrid[2][1] == target_sum and
                subgrid[0][2] + subgrid[1][2] + subgrid[2][2] == target_sum):
            return False

        # Check diagonals
        if not (subgrid[0][0] + subgrid[1][1] + subgrid[2][2] == target_sum and
                subgrid[0][2] + subgrid[1][1] + subgrid[2][0] == target_sum):
            return False
            
        return True

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        if rows < 3 or cols < 3:
            return 0
            
        count = 0
        
        for r in range(rows - 2):
            for c in range(cols - 2):
                current_subgrid = [
                    [grid[r][c], grid[r][c+1], grid[r][c+2]],
                    [grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2]],
                    [grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]]
                ]
                
                if self.is_magic_square(current_subgrid):
                    count += 1
                    
        return count