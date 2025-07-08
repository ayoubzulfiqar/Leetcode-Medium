import collections

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        
        start_row, start_col = entrance[0], entrance[1]
        
        # Queue for BFS: (row, col, steps)
        queue = collections.deque([(start_row, start_col, 0)])
        
        # Set to keep track of visited cells
        visited = set([(start_row, start_col)])
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, steps = queue.popleft()
            
            # Check if current cell is an exit
            # An exit is an empty cell on the border, AND it's not the entrance itself.
            # The 'steps > 0' condition ensures it's not the entrance (since entrance is at steps=0).
            if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and steps > 0:
                return steps
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # Check if not a wall and not visited
                    if maze[nr][nc] == '.' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))
                        
        # If queue becomes empty and no exit is found
        return -1