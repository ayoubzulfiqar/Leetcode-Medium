import math

class Solution:
    def minimizeError(self, nums: list[str], target: int) -> str:
        total_error = 0.0
        current_sum_floor = 0
        diffs = [] 

        for num_str in nums:
            x = float(num_str)
            f = math.floor(x)
            
            current_sum_floor += f
            total_error += (x - f)
            
            if x != f:
                diffs.append(x - f)
        
        diffs.sort(reverse=True)
        
        k_needed = target - current_sum_floor
        
        if k_needed < 0:
            return "-1"
        
        for i in range(k_needed):
            if not diffs:
                return "-1"
            
            d = diffs.pop(0)
            total_error += (1 - 2 * d)
        
        return "{:.3f}".format(total_error)