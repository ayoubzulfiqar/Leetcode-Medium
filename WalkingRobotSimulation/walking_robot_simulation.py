class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Robot's initial position
        x, y = 0, 0

        # Directions: (dx, dy) for North, East, South, West
        # dir_idx = 0: North (0, 1)
        # dir_idx = 1: East (1, 0)
        # dir_idx = 2: South (0, -1)
        # dir_idx = 3: West (-1, 0)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Start facing North

        # Convert obstacles list to a set for O(1) average time complexity lookups
        obstacle_set = set(tuple(o) for o in obstacles)

        # Maximum squared Euclidean distance from the origin
        max_dist_sq = 0

        for command in commands:
            if command == -2:  # Turn left 90 degrees
                dir_idx = (dir_idx + 3) % 4
            elif command == -1:  # Turn right 90 degrees
                dir_idx = (dir_idx + 1) % 4
            else:  # Move forward k units (1 <= k <= 9)
                dx, dy = dirs[dir_idx]
                for _ in range(command):
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in obstacle_set:
                        # If an obstacle is encountered, stay in current location
                        break
                    else:
                        # Move to the new location
                        x, y = next_x, next_y
                        # Update maximum squared distance
                        max_dist_sq = max(max_dist_sq, x*x + y*y)
        
        return max_dist_sq