import collections

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        total_distinct_elements = len(set(nums))
        
        complete_subarrays_count = 0
        
        for i in range(n):
            current_distinct_count = 0
            current_frequency = collections.defaultdict(int)
            
            for j in range(i, n):
                num = nums[j]
                if current_frequency[num] == 0:
                    current_distinct_count += 1
                current_frequency[num] += 1
                
                if current_distinct_count == total_distinct_elements:
                    complete_subarrays_count += (n - j)
                    break
                    
        return complete_subarrays_count