class Solution:
    def minOperationsToMakeMedianK(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        # The median index is n // 2 for both odd and even length arrays
        # according to the problem's definition ("larger of the two values" for even length).
        mid_idx = n // 2
        
        total_operations = 0
        
        # Step 1: Make the element at the median index equal to k.
        # This is a mandatory operation.
        total_operations += abs(nums[mid_idx] - k)
        
        # Step 2: Adjust elements to the left of the median.
        # If nums[mid_idx] was increased to k, elements to its left (nums[i] for i < mid_idx)
        # should ideally be <= k to maintain the sorted property relative to the median.
        # If any nums[i] (i < mid_idx) is currently > k, it must be decreased to k.
        # We iterate from mid_idx - 1 down to 0.
        for i in range(mid_idx - 1, -1, -1):
            if nums[i] > k:
                total_operations += (nums[i] - k)
            else:
                # Since the array is sorted, if nums[i] <= k,
                # then all elements to its left (nums[j] for j < i) will also be <= k.
                # No further operations are needed for elements to the left.
                break
        
        # Step 3: Adjust elements to the right of the median.
        # If nums[mid_idx] was decreased to k, elements to its right (nums[i] for i > mid_idx)
        # should ideally be >= k to maintain the sorted property relative to the median.
        # If any nums[i] (i > mid_idx) is currently < k, it must be increased to k.
        # We iterate from mid_idx + 1 up to n - 1.
        for i in range(mid_idx + 1, n):
            if nums[i] < k:
                total_operations += (k - nums[i])
            else:
                # Since the array is sorted, if nums[i] >= k,
                # then all elements to its right (nums[j] for j > i) will also be >= k.
                # No further operations are needed for elements to the right.
                break
                
        return total_operations