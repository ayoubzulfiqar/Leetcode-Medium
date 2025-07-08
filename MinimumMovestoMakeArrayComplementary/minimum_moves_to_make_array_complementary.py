class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        
        diff = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            
            x = min(a, b)
            y = max(a, b)
            
            # For any target sum T, the initial cost is 2 moves per pair.
            # This is the baseline. We will subtract savings from this.
            
            # If T is in the range [x + 1, y + limit], it takes 1 move.
            # This means a saving of 1 move compared to the 2-move baseline.
            # So, we decrement the cost by 1 for this range.
            diff[x + 1] -= 1
            diff[y + limit + 1] += 1 
            
            # If T is exactly x + y, it takes 0 moves.
            # This means an additional saving of 1 move (total 2 moves saved)
            # compared to the 2-move baseline.
            # So, we decrement the cost by another 1 specifically at x + y.
            diff[x + y] -= 1
            diff[x + y + 1] += 1 
            
        # Initialize current_moves with the maximum possible moves (2 moves per pair)
        current_moves = n 
        min_total_moves = current_moves
        
        # Sweep through all possible target sums from 2 to 2*limit
        for T in range(2, 2 * limit + 1):
            current_moves += diff[T]
            min_total_moves = min(min_total_moves, current_moves)
            
        return min_total_moves