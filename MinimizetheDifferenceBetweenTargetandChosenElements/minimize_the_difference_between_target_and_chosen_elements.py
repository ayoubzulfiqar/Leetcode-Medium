import math

class Solution:
    def minimizeTheDifference(self, mat: list[list[int]], target: int) -> int:
        reachable_sums = set(mat[0])
        
        for r_idx in range(1, len(mat)):
            current_row = mat[r_idx]
            new_reachable_sums = set()
            
            for prev_sum in reachable_sums:
                for num_in_row in current_row:
                    new_reachable_sums.add(prev_sum + num_in_row)
            
            reachable_sums = new_reachable_sums
            
        min_diff = math.inf
        for s in reachable_sums:
            min_diff = min(min_diff, abs(s - target))
            
        return min_diff