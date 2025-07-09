class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        n = len(prices)
        
        if n < 2:
            return 0
            
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
                
        return profit