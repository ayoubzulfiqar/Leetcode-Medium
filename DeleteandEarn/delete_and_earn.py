import collections

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_val = 0
        for num in nums:
            if num > max_val:
                max_val = num

        # points[i] will store the total points earned if we pick number i
        # This effectively sums up all occurrences of a number.
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num

        # Now the problem is transformed into a House Robber problem:
        # Given an array 'points', where points[i] is the value of item i.
        # If you pick item i, you cannot pick item i-1 or item i+1.
        # Maximize the total value.

        # dp[i] = max points considering numbers up to i
        # dp[i] can be:
        # 1. dp[i-1] (if we don't pick i)
        # 2. points[i] + dp[i-2] (if we pick i)
        # So, dp[i] = max(dp[i-1], points[i] + dp[i-2])

        # Base cases for space-optimized DP:
        # prev represents dp[i-2]
        # curr represents dp[i-1]
        prev = 0  # Represents max points up to index -2 (before any valid number)
        curr = 0  # Represents max points up to index -1 (before any valid number)

        for i in range(max_val + 1):
            # new_curr is the max points up to current index i
            # It's max of (not picking i) or (picking i + max points from i-2)
            new_curr = max(curr, points[i] + prev)
            
            # Update prev and curr for the next iteration
            prev = curr
            curr = new_curr
        
        return curr