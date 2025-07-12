class Solution:
    def numRightTriangles(self, grid: list[list[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        row_counts = [0] * R
        col_counts = [0] * C

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
        
        total_triangles = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    # If grid[r][c] is the vertex of the right angle,
                    # we need (row_counts[r] - 1) other '1's in its row
                    # and (col_counts[c] - 1) other '1's in its column.
                    # The -1 is to exclude the current cell itself.
                    
                    # Since grid[r][c] == 1, we are guaranteed that row_counts[r] >= 1
                    # and col_counts[c] >= 1, so the subtractions will not result in negative values.
                    triangles_at_vertex = (row_counts[r] - 1) * (col_counts[c] - 1)
                    total_triangles += triangles_at_vertex
        
        return total_triangles