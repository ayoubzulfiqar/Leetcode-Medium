class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                # We are on an increasing slope, a peak must be to the right
                left = mid + 1
            else:
                # We are on a decreasing slope or at a peak,
                # a peak could be at mid or to its left
                right = mid
        
        # When left == right, we have found a peak element
        return left