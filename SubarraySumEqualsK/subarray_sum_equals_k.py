class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        # A dictionary to store the frequency of each prefix sum
        # Initialize with {0: 1} to handle cases where a subarray
        # starting from index 0 sums to k.
        sum_counts = {0: 1}

        for num in nums:
            current_sum += num
            
            # If (current_sum - k) exists in sum_counts, it means there
            # are sum_counts[current_sum - k] subarrays ending at the
            # current position whose sum is k.
            if current_sum - k in sum_counts:
                count += sum_counts[current_sum - k]
            
            # Add the current_sum to the dictionary or increment its frequency
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1
            
        return count