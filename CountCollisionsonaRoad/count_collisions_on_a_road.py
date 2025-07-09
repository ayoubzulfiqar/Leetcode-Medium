class Solution:
    def countCollisions(self, directions: str) -> int:
        collisions = 0
        pending_R = 0
        has_stationary_point = False

        for char in directions:
            if char == 'R':
                pending_R += 1
            elif char == 'S':
                collisions += pending_R
                pending_R = 0
                has_stationary_point = True
            elif char == 'L':
                if pending_R > 0:
                    collisions += pending_R + 1
                    pending_R = 0
                    has_stationary_point = True
                elif has_stationary_point:
                    collisions += 1
        
        return collisions