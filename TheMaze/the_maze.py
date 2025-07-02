import collections

class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])

        q = collections.deque()
        q.append((start[0], start[1]))

        visited = set()
        visited.add((start[0], start[1]))

        # Directions: (row_change, col_change) for right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c = q.popleft()

            # If the current stopping point is the destination, a path exists
            if r == destination[0] and c == destination[1]:
                return True

            # Explore all possible directions from this stopping point
            for dr, dc in directions:
                # Start rolling from (r, c) in direction (dr, dc)
                nr, nc = r, c
                
                # Keep rolling until a wall or boundary is hit
                while 0 <= nr + dr < rows and \
                      0 <= nc + dc < cols and \
                      maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                
                # (nr, nc) is the new stopping point
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
        
        # If the queue becomes empty and the destination was not reached
        return False