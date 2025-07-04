class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        n = len(colors)
        if n <= 1:
            return 0

        total_time = 0
        
        # Initialize variables for the first balloon in a potential block
        current_sum_for_block = neededTime[0]
        current_max_for_block = neededTime[0]

        # Iterate from the second balloon to compare with the previous one
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                # If the current balloon has the same color as the previous one,
                # it's part of the current consecutive block.
                # Accumulate its time and update the maximum time in this block.
                current_sum_for_block += neededTime[i]
                current_max_for_block = max(current_max_for_block, neededTime[i])
            else:
                # If the current balloon has a different color, the previous block
                # of identical colors has ended.
                # Calculate the cost for the just-ended block:
                # (sum of times of all balloons in the block) - (time of the most expensive balloon to keep)
                total_time += (current_sum_for_block - current_max_for_block)
                
                # Reset for the new block starting with the current balloon 'i'
                current_sum_for_block = neededTime[i]
                current_max_for_block = neededTime[i]
        
        # After the loop finishes, there will be one last block (either a single balloon
        # or a sequence of identical balloons) whose cost needs to be added.
        # This handles cases where the string ends with a block of same colors
        # or a single balloon that was the last element.
        total_time += (current_sum_for_block - current_max_for_block)
        
        return total_time