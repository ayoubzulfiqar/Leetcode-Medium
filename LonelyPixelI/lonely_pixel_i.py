class Solution:
    def findLonelyPixel(self, grid: list[list[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        row_counts = [0] * m
        col_counts = [0] * n

        # First pass: count 'B's in each row and column
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'B':
                    row_counts[r] += 1
                    col_counts[c] += 1

        lonely_pixels = 0
        # Second pass: check for lonely pixels
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'B':
                    # A pixel is lonely if it's the only 'B' in its row and its column
                    if row_counts[r] == 1 and col_counts[c] == 1:
                        lonely_pixels += 1

        return lonely_pixels