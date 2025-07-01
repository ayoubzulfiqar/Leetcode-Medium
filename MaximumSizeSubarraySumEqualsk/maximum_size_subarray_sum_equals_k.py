class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        max_len = 0
        current_sum = 0
        # sum_map stores (prefix_sum: index)
        # Initialize with {0: -1} to handle cases where the subarray
        # starts from index 0 (i.e., the sum from index 0 to i equals k)
        sum_map = {0: -1} 

        for i in range(len(nums)):
            current_sum += nums[i]

            # If (current_sum - k) exists in sum_map, it means
            # there's a subarray from sum_map[current_sum - k] + 1 to i
            # whose sum is k.
            if (current_sum - k) in sum_map:
                max_len = max(max_len, i - sum_map[current_sum - k])
            
            # Store the current_sum and its index if it's the first time we've seen this sum.
            # We only store the first occurrence of a sum because we want the maximum length.
            # If we encounter the same sum again, using its earlier index will always yield
            # a longer (or equal) subarray.
            if current_sum not in sum_map:
                sum_map[current_sum] = i
        
        return max_len