class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n // 2
        
        removed_pairs_count = 0
        
        while left < n // 2 and right < n:
            if nums[left] < nums[right]:
                removed_pairs_count += 1
                left += 1
                right += 1
            else:
                right += 1
        
        return n - 2 * removed_pairs_count