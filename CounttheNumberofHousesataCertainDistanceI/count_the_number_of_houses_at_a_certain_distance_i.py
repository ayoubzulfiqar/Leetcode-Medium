class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        ans = [0] * n

        # Ensure x <= y for consistent calculation
        if x > y:
            x, y = y, x

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                # Calculate distance via the direct linear path
                dist_linear = j - i

                # Calculate distance via the special street (x-y)
                # Path 1: i -> ... -> x -> y -> ... -> j
                # Distance is (distance from i to x) + 1 (for x-y street) + (distance from y to j)
                dist_via_xy = abs(i - x) + 1 + abs(j - y)
                
                # Path 2: i -> ... -> y -> x -> ... -> j
                # Distance is (distance from i to y) + 1 (for y-x street) + (distance from x to j)
                dist_via_yx = abs(i - y) + 1 + abs(j - x)
                
                # The minimum distance between house i and house j
                min_dist = min(dist_linear, dist_via_xy, dist_via_yx)
                
                # Increment the count for this distance
                # Since result is 1-indexed, we use min_dist - 1
                ans[min_dist - 1] += 1

        # Each pair (i, j) with i < j was counted once.
        # Since (house1, house2) and (house2, house1) are distinct pairs,
        # we multiply each count by 2.
        for k in range(n):
            ans[k] *= 2
            
        return ans