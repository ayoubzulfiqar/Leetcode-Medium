import collections

class Solution:
    def maximumSum(self, nums: list[int], m: int, k: int) -> int:
        max_sum = 0
        current_sum = 0
        freq_map = collections.defaultdict(int)
        
        for i in range(k):
            current_sum += nums[i]
            freq_map[nums[i]] += 1
        
        if len(freq_map) >= m:
            max_sum = current_sum
        
        for i in range(k, len(nums)):
            element_out = nums[i - k]
            current_sum -= element_out
            freq_map[element_out] -= 1
            if freq_map[element_out] == 0:
                del freq_map[element_out]
            
            element_in = nums[i]
            current_sum += element_in
            freq_map[element_in] += 1
            
            if len(freq_map) >= m:
                max_sum = max(max_sum, current_sum)
                
        return max_sum