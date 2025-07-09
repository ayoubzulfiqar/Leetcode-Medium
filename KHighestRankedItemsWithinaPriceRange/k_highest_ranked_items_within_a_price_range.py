import collections

class Solution:
    def highestRankedKItems(self, grid: list[list[int]], pricing: list[int], start: list[int], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        low, high = pricing[0], pricing[1]
        start_row, start_col = start[0], start[1]

        q = collections.deque([(0, start_row, start_col)]) # (distance, row, col)
        visited = set([(start_row, start_col)])
        
        # Store (distance, price, row, col) for eligible items
        # Python's default tuple comparison will sort by these criteria in order
        eligible_items = [] 

        # Directions for BFS: up, down, left, right
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            dist, r, c = q.popleft()
            price = grid[r][c]

            # Check if the current cell contains an item within the price range
            if low <= price <= high:
                eligible_items.append((dist, price, r, c))
            
            # Explore neighbors
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # Check bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # Check if not a wall (0) and not visited
                    if grid[nr][nc] != 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((dist + 1, nr, nc))
        
        # Sort the eligible items based on the ranking criteria
        # Python's default tuple sort handles this:
        # 1. Distance (ascending)
        # 2. Price (ascending)
        # 3. Row (ascending)
        # 4. Column (ascending)
        eligible_items.sort()

        # Extract the top k items' coordinates
        result = []
        for i in range(min(k, len(eligible_items))):
            result.append([eligible_items[i][2], eligible_items[i][3]]) # row, col

        return result