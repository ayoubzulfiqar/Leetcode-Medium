class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = 0  # 0: North, 1: East, 2: South, 3: West
        
        # Direction vectors for (dx, dy) corresponding to North, East, South, West
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        for instruction in instructions:
            if instruction == 'G':
                x += dx[direction]
                y += dy[direction]
            elif instruction == 'L':
                direction = (direction + 3) % 4  # Turn left (anti-clockwise)
            elif instruction == 'R':
                direction = (direction + 1) % 4  # Turn right (clockwise)
                
        # The robot is bounded if:
        # 1. It returns to the origin (0, 0) after one cycle.
        # OR
        # 2. It does not return to the origin, but its final direction is not North (0).
        #    If the direction changes, the robot's path will eventually repeat in a cycle
        #    because it will eventually face North again (after 2 or 4 cycles) and
        #    repeat the sequence of moves from a new starting point, but always within a bounded area.
        return (x == 0 and y == 0) or (direction != 0)