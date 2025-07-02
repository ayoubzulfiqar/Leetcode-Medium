class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        distinct_islands = set()
        
        def dfs(r, c, r0, c0, current_island_path):
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited):
                return
            
            visited.add((r, c))
            current_island_path.append((r - r0, c - c0))
            
            dfs(r + 1, c, r0, c0, current_island_path)
            dfs(r - 1, c, r0, c0, current_island_path)
            dfs(r, c + 1, r0, c0, current_island_path)
            dfs(r, c - 1, r0, c0, current_island_path)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_island_path = []
                    dfs(r, c, r, c, current_island_path)
                    current_island_path.sort() 
                    distinct_islands.add(tuple(current_island_path))
                    
        return len(distinct_islands)