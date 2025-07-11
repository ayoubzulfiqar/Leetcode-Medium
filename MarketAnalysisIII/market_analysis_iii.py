class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # buy1: The maximum profit if we are currently holding a stock, having completed at most one transaction.
        #       This is effectively -cost_of_first_stock. Initialized to negative infinity as we haven't bought yet.
        buy1 = float('-inf')

        # sell1: The maximum profit after completing at most one transaction (i.e., bought and sold once).
        #        Initialized to 0, as no transactions yield 0 profit.
        sell1 = 0

        # buy2: The maximum profit if we are currently holding a stock, having completed at most two transactions.
        #       This means we completed the first transaction (profit 'sell1') and then bought a second stock.
        #       Effectively, sell1 - cost_of_second_stock. Initialized to negative infinity.
        buy2 = float('-inf')

        # sell2: The maximum profit after completing at most two transactions (i.e., bought and sold twice).
        #        Initialized to 0.
        sell2 = 0

        for price in prices:
            # Update sell2: Max profit if we sell the second stock today.
            # It's either the previous max profit (sell2) or the profit from selling the stock we bought for the second transaction (buy2 + price).
            sell2 = max(sell2, buy2 + price)

            # Update buy2: Max profit if we buy the second stock today.
            # It's either the previous max profit (buy2) or the profit accumulated after the first transaction (sell1) minus today's price.
            buy2 = max(buy2, sell1 - price)

            # Update sell1: Max profit if we sell the first stock today.
            # It's either the previous max profit (sell1) or the profit from selling the stock we bought for the first transaction (buy1 + price).
            sell1 = max(sell1, buy1 + price)

            # Update buy1: Max profit if we buy the first stock today.
            # It's either the previous max profit (buy1) or simply buying today's stock (which means a cost of -price).
            buy1 = max(buy1, -price)

        # The maximum profit after at most two transactions will be in sell2.
        return sell2

```