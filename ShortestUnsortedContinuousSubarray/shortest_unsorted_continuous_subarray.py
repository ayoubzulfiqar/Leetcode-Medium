class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        start = 0
        while start < n - 1 and nums[start] <= nums[start + 1]:
            start += 1

        if start == n - 1:
            return 0

        end = n - 1
        while end > 0 and nums[end] >= nums[end - 1]:
            end -= 1

        min_val_in_subarray = float('inf')
        max_val_in_subarray = float('-inf')
        for i in range(start, end + 1):
            min_val_in_subarray = min(min_val_in_subarray, nums[i])
            max_val_in_subarray = max(max_val_in_subarray, nums[i])

        while start > 0 and nums[start - 1] > min_val_in_subarray:
            start -= 1

        while end < n - 1 and nums[end + 1] < max_val_in_subarray:
            end += 1

        return end - start + 1