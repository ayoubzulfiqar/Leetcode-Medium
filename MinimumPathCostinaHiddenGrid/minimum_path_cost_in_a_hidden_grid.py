import collections
import heapq

class GridMaster:
    def canMove(self, direction: str) -> bool:
        """
        Checks if a move in the given direction is possible.
        """
        pass

    def move(self, direction: str) -> int:
        """
        Moves in the given direction and returns the cost of moving to the new cell.
        """
        pass

    def isTarget(self) -> bool:
        """
        Checks if the current cell is a target cell.
        """
        pass

class Solution:
    def findMinimumPath(self, master: 'GridMaster') -> int:
        # --- Step 1: Explore the grid and build the map ---
        # grid_map: Stores (r, c) -> cost of cell (cost incurred upon entering the cell)
        grid_map = {}
        # target_cells: Stores (r, c) coordinates of all discovered target cells
        target_cells = set()
        
        # Define directions and their corresponding (dr, dc) changes and opposite directions
        # This helps in both moving and backtracking.
        # Format: (dr, dc, opposite_direction_char)
        directions_map = {
            'U': (-1, 0, 'D'),
            'D': (1, 0, 'U'),
            'L': (0, -1, 'R'),
            'R': (0, 1, 'L')
        }

        # DFS function to explore the grid and populate grid_map and target_cells
        # `r, c`: current coordinates in our conceptual grid map
        def dfs(r: int, c: int):
            # If the current cell is a target, add it to our set of target cells
            if master.isTarget():
                target_cells.add((r, c))
            
            # Iterate through all possible directions (Up, Down, Left, Right)
            for direction_char, (dr, dc, opposite_direction_char) in directions_map.items():
                nr, nc = r + dr, c + dc # Calculate coordinates of the next cell

                # Check if the next cell has not been visited yet and if a move is possible
                if (nr, nc) not in grid_map and master.canMove(direction_char):
                    # Move to the new cell and get the cost of entering it
                    move_cost = master.move(direction_char)
                    # Store the cost of the new cell in our map
                    grid_map[(nr, nc)] = move_cost
                    
                    # Recursively call DFS for the new cell
                    dfs(nr, nc)
                    
                    # Backtrack: move back to the current cell to explore other paths
                    master.move(opposite_direction_char)

        # Start DFS from the initial position (0,0).
        # The cost of the starting cell itself is considered 0 for path calculation.
        grid_map[(0,0)] = 0 
        dfs(0, 0)

        # If no target cells were found during exploration, it's impossible to reach any target.
        if not target_cells:
            return -1

        # --- Step 2: Run Dijkstra's algorithm on the discovered map ---
        # dist: Dictionary to store the minimum cost to reach each cell from (0,0)
        # Initialize all distances to infinity, except for the starting cell (0,0).
        dist = collections.defaultdict(lambda: float('inf'))
        dist[(0,0)] = 0
        
        # Priority queue for Dijkstra's. Stores tuples: (current_total_cost, r, c)
        # We use a min-heap to always extract the node with the smallest cost.
        pq = [(0, 0, 0)] # Start from (0,0) with accumulated cost 0

        # Variable to store the minimum path cost found to any target cell
        min_path_cost_to_target = float('inf')

        while pq:
            current_total_cost, r, c = heapq.heappop(pq)

            # If we've already found a shorter path to (r, c), skip this one
            if current_total_cost > dist[(r, c)]:
                continue

            # If the current cell is one of our target cells, update the minimum cost found so far
            if (r, c) in target_cells:
                min_path_cost_to_target = min(min_path_cost_to_target, current_total_cost)

            # Explore all 4 neighbors (Up, Down, Left, Right)
            for direction_char, (dr, dc, _) in directions_map.items():
                nr, nc = r + dr, c + dc

                # Check if the neighbor cell exists in our discovered grid map
                if (nr, nc) in grid_map:
                    # The cost to move to (nr, nc) is the cost of cell (nr, nc) itself
                    cost_to_enter_neighbor = grid_map[(nr, nc)]
                    
                    # Calculate the new total cost to reach (nr, nc) through (r, c)
                    new_total_cost = current_total_cost + cost_to_enter_neighbor

                    # If this new path is shorter than the previously known shortest path to (nr, nc)
                    if new_total_cost < dist[(nr, nc)]:
                        dist[(nr, nc)] = new_total_cost # Update the distance
                        heapq.heappush(pq, (new_total_cost, nr, nc)) # Add to priority queue

        # After Dijkstra's finishes, return the minimum cost found to any target.
        # If min_path_cost_to_target is still infinity, it means no target was reachable.
        return min_path_cost_to_target if min_path_cost_to_target != float('inf') else -1