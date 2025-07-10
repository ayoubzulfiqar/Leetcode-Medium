class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: list[int]) -> list[int]:
        memo = {}

        def find_max_points(idx, arrows_left):
            if idx == -1:
                return 0
            
            if (idx, arrows_left) in memo:
                return memo[(idx, arrows_left)]

            # Option 1: Bob does not win section 'idx'.
            # He shoots 0 arrows for this section.
            points_if_lose = find_max_points(idx - 1, arrows_left)

            # Option 2: Bob tries to win section 'idx'.
            # He needs aliceArrows[idx] + 1 arrows to win this section.
            points_if_win = -1  # Initialize as not possible
            arrows_needed = aliceArrows[idx] + 1
            
            if arrows_left >= arrows_needed:
                points_if_win = idx + find_max_points(idx - 1, arrows_left - arrows_needed)
            
            result = max(points_if_lose, points_if_win)
            memo[(idx, arrows_left)] = result
            return result

        # Populate the memoization table by calling the DP function.
        find_max_points(11, numArrows)

        # Reconstruct the bobArrows array based on the decisions made.
        bob_arrows_result = [0] * 12
        current_arrows_left = numArrows

        # Iterate from the highest scoring section (11) down to the lowest (0).
        for idx in range(11, -1, -1):
            # Points if Bob loses section 'idx'
            points_if_lose