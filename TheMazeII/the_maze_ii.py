import collections

class Solution:
    def shortestDistance(self, maze: list[list[int]], start: list[int], destination: list[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        # Initialize distances with infinity for all cells
        distances = [[float('inf')] * cols for _ in range(rows)]

        # Directions for movement: (dr, dc) for right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Queue for BFS: stores (row, col, current_distance)
        queue = collections.deque()

        # The starting point has a distance of 0
        distances[start[0]][start[1]] = 0
        queue.append((start[0], start[1], 0))

        while queue:
            r, c, current_dist = queue.popleft()

            # If we have already found a shorter path to this cell (r, c),
            # we can skip processing this path as it's not optimal.
            if current_dist > distances[r][c]:
                continue

            # Explore all four possible rolling directions from the current cell (r, c)
            for dr, dc in directions:
                next_r, next_c = r, c
                steps = 0

                # Simulate the ball rolling in the current direction until it hits a wall or boundary
                while True:
                    temp_r, temp_c = next_r + dr, next_c + dc

                    # Check if the next potential cell is within maze boundaries and is not a wall
                    if 0 <= temp_r < rows and 0 <= temp_c < cols and maze[temp_r][temp_c] == 0:
                        next_r, next_c = temp_r, temp_c  # Continue rolling
                        steps += 1
                    else:
                        # Ball hit a wall or boundary, it stops at (next_r, next_c)
                        break
                
                # Calculate the new distance to the cell where the ball stopped
                new_dist = current_dist + steps

                # If this new path to (next_r, next_c) is shorter than any previously found path
                if new_dist < distances[next_r][next_c]:
                    distances[next_r][next_c] = new_dist  # Update the shortest distance
                    queue.append((next_r, next_c, new_dist)) # Add to queue for further exploration

        # After the BFS completes, the distance to the destination cell will be the shortest distance found.
        result_dist = distances[destination[0]][destination[1]]

        # If the destination was unreachable, its distance will still be float('inf').
        # In that case, return -1; otherwise, return the found distance.
        return result_dist if result_dist != float('inf') else -1