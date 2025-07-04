import math

class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        
        # min_len_at_or_before[i] stores the minimum length of a subarray
        # with sum 'target' that ends at or before index 'i'.
        # Initialize with infinity.
        min_len_at_or_before = [math.inf] * n
        
        # Dictionary to store prefix sums and their first occurring index.
        # {prefix_sum: index}
        # Initialize with {0: -1} to handle subarrays starting from index 0.
        prefix_sums = {0: -1}
        
        current_sum = 0
        min_overall_length_sum = math.inf
        
        for i in range(n):
            current_sum += arr[i]
            
            # min_len_current_pos will store the length of a subarray
            #