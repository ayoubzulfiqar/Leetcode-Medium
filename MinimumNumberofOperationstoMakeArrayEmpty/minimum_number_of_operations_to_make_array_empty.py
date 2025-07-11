import collections

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        
        total_operations = 0
        
        for count in counts.values():
            if count == 1:
                return -1
            
            ops_for_current_count = count // 3
            if count % 3 != 0:
                ops_for_current_count += 1
            
            total_operations += ops_for_current_count
            
        return total_operations