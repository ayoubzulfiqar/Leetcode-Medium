class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        # Kadane's algorithm to find the maximum subarray sum
        # max_so_far stores the maximum sum found so far.
        # current_max stores the maximum sum of a subarray ending at the current position.
        max_so_far = -float('inf')
        current_max = 0
        for x in nums:
            current_max += x
            max_so_far = max(max_so_far, current_max)
            # If current_max becomes negative, it means this subarray sum
            # is pulling down the total sum, so we reset it to 0 to start a new subarray.
            # This ensures we only consider positive-contributing subarrays for max_so_far.
            if current_max < 0:
                current_max = 0

        # Kadane's algorithm to find the minimum subarray sum
        # min_so_far stores the minimum sum found so far.
        # current_min stores the minimum sum of a subarray ending at the current position.
        min_so_far = float('inf')
        current_min = 0
        for x in nums:
            current_min += x
            min_so_far = min(min_so_far, current_min)
            # If current_min becomes positive, it means this subarray sum
            # is pushing up the total sum, so we reset it to 0 to start a new subarray.
            # This ensures we only consider negative-contributing subarrays for min_so_far.
            if current_min > 0:
                current_min = 0
        
        # The maximum absolute sum is the maximum of the absolute value of 
        # the maximum subarray sum and the absolute value of the minimum subarray sum.
        # This covers cases where the largest absolute sum comes from a positive sum
        # (e.g., [2,3] -> 5) or a negative sum (e.g., [-5,1,-4] -> -8, abs(-8)=8).
        return max(max_so_far, abs(min_so_far))