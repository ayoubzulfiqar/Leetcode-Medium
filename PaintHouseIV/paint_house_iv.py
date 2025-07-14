import math

class Solution:
    def minCost(self, n: int, cost: list[list[int]]) -> int:
        prev_dp = [[math.inf] * 3 for _ in range(3)]

        # Base case: i = 0 (houses 0 and n-1)
        # c0 is the color for house 0
        # c_n_minus_1 is the color for house n-1
        for c0 in range(3):
            for c_n_minus_1 in range(3):
                # Condition: Houses equidistant from ends must not be painted the same color
                if c0 != c_n_minus_1:
                    prev_dp[c0][c_n_minus_1] = cost[0][c0] + cost[n-1][c_n_minus_1]
        
        # Iterate for subsequent pairs of houses (i, n-1-i)
        # The loop runs