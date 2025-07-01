class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        # prev_hold: maximum profit ending on the previous day, holding a stock
        # prev_sold: maximum profit ending on the previous day, having just sold a stock
        # prev_rest: maximum profit ending on the previous day, in a rest/cooldown state

        # Initialize states for day 0
        # If we buy on day 0, profit is -prices[0]
        prev_hold = -prices[0]
        # Cannot have sold on day 0 without buying first
        prev_sold = float('-inf') 
        # Start with 0 profit and no stock (rest state)
        prev_rest = 0             

        for i in range(1, n):
            # Calculate current day's states based on previous day's states
            
            # curr_hold: Max profit if holding a stock at the end of day i
            # Option 1: Continue holding from previous day (prev_hold)
            # Option 2: Buy today (prev_rest - prices[i], as we must be in rest state yesterday to buy today)
            curr_hold = max(prev_hold, prev_rest - prices[i])
            
            # curr_sold: Max profit if selling a stock at the end of day i
            # Must have held stock yesterday and sell it today (prev_hold + prices[i])
            curr_sold = prev_hold + prices[i]
            
            # curr_rest: Max profit if in a rest state at the end of day i
            # Option 1: Was in rest state yesterday (prev_rest)
            # Option 2: Just sold yesterday, so today is cooldown (prev_sold)
            curr_rest = max(prev_rest, prev_sold)

            # Update previous states for the next iteration
            prev_hold = curr_hold
            prev_sold = curr_sold
            prev_rest = curr_rest
        
        # The maximum profit will be either from having sold on the last day,
        # or being in a rest state (meaning we sold before the last day or never bought).
        # We cannot end holding a stock for maximum profit.
        return max(prev_sold, prev_rest)