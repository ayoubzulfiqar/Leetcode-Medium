class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        max_day = days[-1]
        
        dp = [0] * (max_day + 1)
        
        travel_days_set = set(days)
        
        cost_1_day = costs[0]
        cost_7_day = costs[1]
        cost_30_day = costs[2]
        
        for i in range(1, max_day + 1):
            if i not in travel_days_set:
                dp[i] = dp[i-1]
            else:
                option1_cost = dp[i-1] + cost_1_day
                option2_cost = dp[max(0, i-7)] + cost_7_day
                option3_cost = dp[max(0, i-30)] + cost_30_day
                
                dp[i] = min(option1_cost, option2_cost, option3_cost)
                
        return dp[max_day]