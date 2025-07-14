class Solution:
    def fillSpecialGrid(self, n: int) -> list[list[int]]:
        if n == 0:
            return [[0]]

        prev_grid = self.fillSpecialGrid(n - 1)

        prev_size = 2**(n - 1)
        
        offset = prev_size * prev_size

        current_size = 2**n
        grid = [[0] * current_size for _ in range(current_size)]

        for r in range(prev_size):
            for c in range(prev_size):
                grid[r][c + prev_size] = prev_grid[r][c] + (0 * offset)

                grid[r + prev_size][c + prev_size] = prev_grid[r][c] + (1 * offset)

                grid[r + prev_size][c] = prev_grid[r][c] + (2 * offset)

                grid[r][c] = prev_grid[r][c] + (3 * offset)
        
        return grid