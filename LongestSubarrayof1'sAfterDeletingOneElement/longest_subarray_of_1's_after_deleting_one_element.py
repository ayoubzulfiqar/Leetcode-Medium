class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # The current window [left, right] contains at most one zero.
            # The length of the subarray of 1's after deleting one element
            # (either the zero if it exists, or one of the 1's if no zero exists)
            # is (right - left).
            max_len = max(max_len, right - left)
        
        return max_len