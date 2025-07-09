import math

class Solution:
    def minCostToBuyApples(self, cost: list[int], k: int) -> int:
        n = len(cost)
        dp = [math.inf] * (k + 1)
        dp[0] = 0

        for i in range(1, k + 1):
            for j in range(n):
                apples_in_bundle = j + 1
                bundle_cost = cost[j]

                if i >= apples_in_bundle:
                    if dp[i - apples_in_bundle] != math.inf:
                        dp[i] = min(dp[i], dp[i - apples_in_bundle] + bundle_cost)
        
        return dp[k] if dp[k] != math.inf else -1