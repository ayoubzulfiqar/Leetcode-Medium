class Solution:
    def maxPoints(self, n: int, k: int, stayScore: list[list[int]], travelScore: list[list[int]]) -> int:
        dp = [[0] * n for _ in range(k)]

        for j in range(n):
            dp[0][j] = stayScore[0][j]

        for i in range(1, k):
            for j in range(n):
                stay_option = dp[i-1][j] + stayScore[i][j]
                
                max_travel_option = -1 

                for p in range(n):
                    if p != j:
                        max_travel_option = max(max_travel_option, dp[i-1][p] + travelScore[p][j])
                
                dp[i][j] = max(stay_option, max_travel_option)
        
        return max(dp[k-1])