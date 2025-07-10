class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        total_cells = n * n

        if grid[0][0] != 0:
            return False

        positions = [None] * total_cells
        for r in range(n):
            for c in range(n):
                positions[grid[r][c]] = (r, c)

        for k in range(total_cells - 1):
            r1, c1 = positions[k]
            r2, c2 = positions[k+1]

            dr = abs(r1 - r2)
            dc = abs(c1 - c2)

            if not ((dr == 1 and dc == 2) or (dr == 2 and dc == 1)):
                return False
        
        return True