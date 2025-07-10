import bisect

class Solution:
    def maximizeTheProfit(self, n: int, offers: list[list[int]]) -> int:
        offers.sort(key=lambda x: x[1])

        dp = [(0, 0)]

        for start, end, gold in offers:
            idx = bisect.bisect_right(dp, start, key=lambda x: x[0]) - 1
            
            profit_if_taken = gold + dp[idx][1]
            profit_if_not_taken = dp[-1][1]

            new_max_profit = max(profit_if_taken, profit_if_not_taken)

            if new_max_profit > dp[-1][1]:
                dp.append((end + 1, new_max_profit))

        return dp[-1][1]