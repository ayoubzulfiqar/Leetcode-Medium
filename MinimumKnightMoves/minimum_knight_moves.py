import collections

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Normalize the target coordinates to the first quadrant (x >= 0, y >= 0)
        # and ensure x >= y due to symmetry.
        target_x = abs(x)
        target_y = abs(y)

        # Optimization: If target_x < target_y, swap them.
        # This ensures target_x is always the larger or equal coordinate.
        if target_x < target_y:
            target_x, target_y = target_y, target_x

        # Base case: If target is (0,0), 0 moves are needed.
        if target_x == 0 and target_y == 0:
            return 0

        # Knight moves: (dx, dy)
        # These are the 8 possible moves a knight can make.
        knight_moves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        # BFS queue: stores ((current_x, current_y), moves)
        # Start from (0,0) with 0 moves.
        queue = collections.deque([((0, 0), 0)])

        # Visited set: stores normalized coordinates (max(abs(x), abs(y)), min(abs(x), abs(y)))
        # to avoid redundant computations and cycles.
        # The initial state (0,0) is already normalized.
        visited = set([(0, 0)])

        while queue:
            (curr_x, curr_y), moves = queue.popleft()

            # Explore all 8 possible knight moves from the current actual position
            for dx, dy in knight_moves:
                next_x, next_y = curr_x + dx, curr_y + dy

                # Normalize the next position for checking against target and visited set.
                # We use max(abs(x), abs(y)) and min(abs(x), abs(y)) for the normalized state.
                # This is crucial for correctly handling symmetry.
                normalized_next_x = abs(next_x)
                normalized_next_y = abs(next_y)
                
                # Ensure the larger coordinate is first for consistent normalization
                if normalized_next_x < normalized_next_y:
                    normalized_next_x, normalized_next_y = normalized_next_y, normalized_next_x
                
                normalized_next_pos = (normalized_next_x, normalized_next_y)

                # If the normalized next position is the target, we found the shortest path
                if normalized_next_pos == (target_x, target_y):
                    return moves + 1

                # If the normalized next position has not been visited, add it to the queue
                # and mark as visited.
                if normalized_next_pos not in visited:
                    visited.add(normalized_next_pos)
                    # Store the actual (next_x, next_y) in the queue for subsequent moves,
                    # as knight moves are relative to the actual coordinates.
                    queue.append(((next_x, next_y), moves + 1))

        # This part should ideally not be reached as a path always exists on an infinite board.
        return -1