import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        MOD = 10**9 + 7

        initial_sum = 0
        max_reduction = 0

        sorted_nums1 = sorted(nums1)

        for i in range(n):
            original_diff = abs(nums1[i] - nums2[i])
            initial_sum += original_diff

            idx = bisect.bisect_left(sorted_nums1, nums2[i])

            min_diff_at_i = float('inf')

            if idx < n:
                min_diff_at_i = min(min_diff_at_i, abs(sorted_nums1[idx] - nums2[i]))
            
            if idx > 0:
                min_diff_at_i = min(min_diff_at_i, abs(sorted_nums1[idx - 1] - nums2[i]))
            
            max_reduction = max(max_reduction, original_diff - min_diff_at_i)
        
        return (initial_sum - max_reduction) % MOD