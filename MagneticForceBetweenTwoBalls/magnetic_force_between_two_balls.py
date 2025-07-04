class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()

        def check(min_force: int) -> bool:
            """
            Checks if it's possible to place 'm' balls such that the
            minimum magnetic force between any two balls is at least 'min_force'.
            """
            count = 1  # Place the first ball at the first position
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True  # Found enough positions
            return count >= m

        # The possible range for the minimum magnetic force
        # Minimum possible force is 1 (if positions are consecutive)
        # Maximum possible force is the distance between the first and last basket
        low = 1
        high = position[-1] - position[0]
        
        ans = 0

        # Binary search for the maximum possible minimum force
        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                # If 'mid' is achievable, try for a larger minimum force
                ans = mid
                low = mid + 1
            else:
                # If 'mid' is not achievable, reduce the minimum force
                high = mid - 1
        
        return ans