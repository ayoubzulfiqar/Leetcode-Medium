import collections

class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = collections.deque()

        # Add all land cells on the boundary to the queue and mark them as visited (0)
        # Process top and bottom rows
        for c in range(cols):
            if grid[0][c] == 1:
                q.append((0, c))
                grid[0][c] = 0
            if grid[rows - 1][c] == 1:
                q.append((rows - 1, c))
                grid[rows - 1][c] = 0

        # Process left and right columns (excluding corners already handled by row processing)
        for r in range(1, rows - 1):
            if grid[r][0] == 1:
                q.append((r, 0))
                grid[r][0] = 0
            if grid[r][cols - 1] == 1:
                q.append((r, cols - 1))
                grid[r][cols - 1] = 0

        # Directions for 4-directional movement: (row_offset, col_offset)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Perform BFS to find all land cells connected to the boundary
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check if the neighbor is within bounds and is a land cell (1)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0 # Mark as visited/sunk
                    q.append((nr, nc))

        # Count the remaining land cells (these are the enclaves)
        enclaves_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    enclaves_count += 1

        return enclaves_count