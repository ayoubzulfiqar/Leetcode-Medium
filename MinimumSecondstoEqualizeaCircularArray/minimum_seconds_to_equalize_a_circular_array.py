import collections

class Solution:
    def minimumSeconds(self, nums: list[int]) -> int:
        n = len(nums)
        
        val_to_indices = collections.defaultdict(list)
        for i, num in enumerate(nums):
            val_to_indices[num].append(i)
        
        if len(val_to_indices) == 1:
            return 0
            
        min_total_seconds = float('inf')
        
        for val, indices in val_to_indices.items():
            max_gap_seconds_for_val = 0
            
            m = len(indices)
            
            if m == 1:
                max_gap_seconds_for_val = n // 2
            else:
                for k in range(m - 1):
                    gap_dist = indices[k+1] - indices[k]
                    max_gap_seconds_for_val = max(max_gap_seconds_for_val, (gap_dist + 1) // 2)
                
                circular_gap_dist = n - indices[m-1] + indices[0]
                max_gap_seconds_for_val = max(max_gap_seconds_for_val, (circular_gap_dist + 1) // 2)
            
            min_total_seconds = min(min_total_seconds, max_gap_seconds_for_val)
            
        return min_total_seconds