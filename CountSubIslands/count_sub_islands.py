import collections

class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        
        sub_island_count = 0
        
        # Directions for 4-directional movement (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for r in range(rows):
            for c in range(cols):
                # If we find a land cell (1) in grid2 that hasn't been visited yet
                if grid2[r][c] == 1:
                    # Start BFS to explore this grid2 island
                    q = collections.deque()
                    q.append((r, c))
                    grid2[r][c] = 0 # Mark as visited by changing 1 to 0
                    
                    is_current_island_sub = True
                    
                    # BFS traversal to find all connected land cells in this grid2 island
                    while q:
                        curr_r, curr_c = q.popleft()
                        
                        # Check if the current cell in grid2 is also land in grid1
                        # If grid1[curr_r][curr_c] is 0, then this grid2 island cannot be a sub-island
                        if grid1[curr_r][curr_c] == 0:
                            is_current_island_sub = False 
                        
                        # Explore neighbors
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            # If neighbor is within bounds, is land in grid2, and not yet visited
                            if 0 <= nr < rows and 0 <= nc < cols and grid2[nr][nc] == 1:
                                q.append((nr, nc))
                                grid2[nr][nc] = 0 # Mark as visited
                    
                    # After exploring the entire grid2 island, check if it qualified as a sub-island
                    if is_current_island_sub:
                        sub_island_count += 1
                        
        return sub_island_count