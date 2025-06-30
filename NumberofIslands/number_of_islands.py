import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0

        # Directions for exploring neighbors (down, up, right, left)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    
                    # Start BFS from this land cell
                    q = collections.deque([(r, c)])
                    grid[r][c] = '0'  # Mark the cell as visited by changing it to '0'

                    while q:
                        curr_r, curr_c = q.popleft()

                        # Explore all four adjacent directions
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc

                            # Check if the neighbor is within bounds and is land ('1')
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'  # Mark as visited
                                q.append((nr, nc))
        
        return num_islands