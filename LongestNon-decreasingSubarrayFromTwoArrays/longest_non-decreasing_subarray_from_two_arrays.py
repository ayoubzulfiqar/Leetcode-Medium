class Solution:
    def longestNonDecreasingSubarray(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        if n == 0:
            return 0
        
        prev_dp1 = 1  # Length of longest non-decreasing subarray ending at previous index, choosing nums1[i-1]
        prev_dp2 = 1  # Length of longest non-decreasing subarray ending at previous index, choosing nums2[i-1]
        max_len = 1   # Overall maximum length found so far
        
        for i in range(1, n):
            current_dp1 = 1  # Length of longest non-decreasing subarray ending at current index, choosing nums1[i]
            current_dp2 = 1  # Length of longest non-decreasing subarray ending at current index, choosing nums2[i]
            
            # Calculate current_dp1: if nums1[i] is chosen at current index
            # It can extend a subarray ending with nums1[i-1]
            if nums1[i] >= nums1[i-1]:
                current_dp1 = max(current_dp1, prev_dp1 + 1)
            # It can extend a subarray ending with nums2[i-1]
            if nums1[i] >= nums2[i-1]:
                current_dp1 = max(current_dp1, prev_dp2 + 1)
            
            # Calculate current_dp2: if nums2[i] is chosen at current index
            # It can extend a subarray ending with nums1[i-1]
            if nums2[i] >= nums1[i-1]:
                current_dp2 = max(current_dp2, prev_dp1 + 1)
            # It can extend a subarray ending with nums2[i-1]
            if nums2[i] >= nums2[i-1]:
                current_dp2 = max(current_dp2, prev_dp2 + 1)
            
            # Update the overall maximum length
            max_len = max(max_len, current_dp1, current_dp2)
            
            # Update previous DP values for the next iteration
            prev_dp1 = current_dp1
            prev_dp2 = current_dp2
            
        return max_len