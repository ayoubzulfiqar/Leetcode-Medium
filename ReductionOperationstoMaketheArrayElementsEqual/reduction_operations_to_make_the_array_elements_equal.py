import collections

class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        
        unique_sorted_values = sorted(counts.keys())
        
        operations = 0
        
        for i in range(1, len(unique_sorted_values)):
            current_value = unique_sorted_values[i]
            operations += counts[current_value] * i
            
        return operations