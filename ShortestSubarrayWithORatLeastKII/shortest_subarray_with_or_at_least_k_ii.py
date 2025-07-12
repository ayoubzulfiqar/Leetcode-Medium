import math

class Solution:
    def shortestSubarrayWithORAtLeastK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_len = float('inf')
        
        # current_ors will store a list of (OR_value, start_index) pairs.
        # For a given 'right' pointer, this list represents all distinct OR values
        # of subarrays ending at 'right', along with their corresponding starting indices.
        # The list is maintained such that:
        # 1. The OR_value is strictly increasing.
        # 2. The start_index is strictly decreasing.
        # This structure ensures that for each distinct OR_value, we store the
        # *rightmost* (i.e., shortest) subarray that achieves that OR_value.
        current_ors = [] 
        
        for right in range(n):
            # new_ors_list will store the updated (OR_value, start_index) pairs for subarrays ending at 'right'.
            new_ors_list = []
            
            # 1. The subarray consisting only of nums[right] is the shortest subarray ending at 'right'.
            # Its OR value is nums[right] and its start index is 'right'.
            new_ors_list.append((nums[right], right))
            
            # 2. Extend previous subarrays by ORing with nums[right].
            # Iterate through the current_ors (which holds pairs for subarrays ending at 'right - 1').
            for val, start_idx in current_ors:
                new_val = val | nums[right]
                
                # We only add this (new_val, start_idx) pair if new_val is distinct from the last OR value
                # added to new_ors_list.
                # This ensures that new_ors_list maintains strictly increasing OR values.
                # Since current_ors is processed from shortest to longest subarrays (by start_idx decreasing),
                # if new_val is the same as