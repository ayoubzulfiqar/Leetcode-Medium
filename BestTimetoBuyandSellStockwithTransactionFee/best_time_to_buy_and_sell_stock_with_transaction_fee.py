class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        # cash: maximum profit if we do not hold a stock on the current day
        # hold: maximum profit if we hold a stock on the current day
        
        # Initialize for the first day (day 0)
        # If we have stock on day 0, we must have bought it.
        hold = -prices[0] 
        # If we don't have stock on day 0, profit is 0.
        cash = 0

        # Iterate from the second day (day 1) up to the last day
        for i in range(1, n):
            # Calculate the new cash state:
            # Option 1: Remain in cash state (do nothing)
            # Option 2: Sell the stock we were holding (previous hold + current price - transaction fee)
            new_cash = max(cash, hold + prices[i] - fee)
            
            # Calculate the new hold state:
            # Option 1: Remain in hold state (do nothing)
            # Option 2: Buy a stock (previous cash - current price)
            new_hold = max(hold, cash - prices[i])
            
            # Update the states for the next iteration
            cash = new_cash
            hold = new_hold
            
        # The maximum profit is achieved when we end up with no stock (in the cash state).
        return cash