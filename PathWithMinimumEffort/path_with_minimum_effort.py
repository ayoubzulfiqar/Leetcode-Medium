import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        # dist[r][c] stores the minimum effort required to reach cell (r, c)
        # from the top-left cell (0, 0).
        # Initialize all distances to infinity.
        dist = [[float('inf')] * cols for _ in range(rows)]
        
        # The effort to reach the starting cell (0, 0) is 0.
        dist[0][0] = 0

        # Priority queue stores tuples of (effort, row, col).
        # It will always pop the cell with the minimum effort found so far.
        pq = [(0, 0, 0)]  # (effort_to_reach_this_cell, current_row, current_col)

        # Define directions for moving up, down, left, right.
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while pq:
            current_effort, r, c = heapq.heappop(pq)

            # If we have already found a path to (r, c) with less effort,
            # then we don't need to process this path as it's suboptimal.
            if current_effort > dist[r][c]:
                continue

            # If we have reached the destination cell (bottom-right),
            # this is the minimum effort required for a path to it.
            if r == rows - 1 and c == cols - 1:
                return current_effort

            # Explore all four possible neighbors (up, down, left, right)
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # Check if the neighbor is within the grid boundaries.
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Calculate the effort required to move from (r, c) to (nr, nc).
                    # This is the absolute difference in heights.
                    edge_effort = abs(heights[r][c] - heights[nr][nc])
                    
                    # The effort of the path to (nr, nc) through (r, c) is the maximum
                    # of the effort to reach (r, c) and the effort to traverse the edge (r,c) to (nr,nc).
                    new_effort = max(current_effort, edge_effort)

                    # If this new path offers less effort to reach (nr, nc) than
                    # any previously found path, update the distance and push to the priority queue.
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
        
        # This line should ideally not be reached if a path always exists,
        # as the destination (rows-1, cols-1) will be popped and returned.
        # However, as a fallback, return the calculated effort to the destination.
        return dist[rows - 1][cols - 1]