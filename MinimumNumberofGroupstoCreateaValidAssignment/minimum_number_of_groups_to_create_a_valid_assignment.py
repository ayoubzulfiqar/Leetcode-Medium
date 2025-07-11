import collections

class Solution:
    def minGroupsForValidAssignment(self, balls: list[int]) -> int:
        counts = collections.Counter(balls)
        
        min_freq = min(counts.values())
        
        min_total_groups = float('inf')
        
        for k in range(1, min_freq + 1):
            current_total_groups = 0
            is_k_valid = True
            
            for f in counts.values():
                min_Nf = (f + k) // (k + 1)
                max_Nf = f // k
                
                if min_Nf > max_Nf:
                    is_k_valid = False
                    break
                
                current_total_groups += min_Nf
            
            if is_k_valid:
                min_total_groups = min(min_total_groups, current_total_groups)
                
        return min_total_groups