class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        max_len = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])
        
        return max_len