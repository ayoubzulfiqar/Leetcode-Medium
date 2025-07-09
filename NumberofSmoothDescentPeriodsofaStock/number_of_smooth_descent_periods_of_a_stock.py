class Solution:
    def smoothDescentPeriods(self, prices: list[int]) -> int:
        total_smooth_periods = 0
        current_smooth_descent_length = 0

        for i in range(len(prices)):
            if i == 0 or prices[i-1] - prices[i] != 1:
                # If it's the first element or the smooth descent sequence is broken,
                # start a new sequence of length 1 (the current day itself).
                current_smooth_descent_length = 1
            else: # prices[i-1] - prices[i] == 1
                # If the current day continues the smooth descent, extend the current sequence.
                current_smooth_descent_length += 1
            
            # Add the number of smooth descent periods ending at the current day 'i'.
            # A sequence of length 'L' ending at 'i' contributes 'L' smooth descent periods:
            # the period of length 1 (ending at i), length 2 (ending at i), ..., length L (ending at i).
            total_smooth_periods += current_smooth_descent_length
            
        return total_smooth_periods