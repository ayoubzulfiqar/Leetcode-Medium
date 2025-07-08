import collections

class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        dp = [0] * (n + 1)
        
        rides_by_end_point = collections.defaultdict(list)
        for start, end, tip in rides:
            earnings = end - start + tip
            rides_by_end_point[end].append((start, earnings))
            
        for i in range(1, n + 1):
            dp[i] = dp[i-1]
            
            if i in rides_by_end_point:
                for start, earnings in rides_by_end_point[i]:
                    dp[i] = max(dp[i], dp[start] + earnings)
                    
        return dp[n]