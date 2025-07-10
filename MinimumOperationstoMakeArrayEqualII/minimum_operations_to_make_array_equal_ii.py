class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n = len(nums1)

        if k == 0:
            return 0 if nums1 == nums2 else -1

        pos_sum = 0
        neg_sum = 0

        for i in range(n):
            diff = nums1[i] - nums2[i]
            
            if diff % k != 0:
                return -1
            
            if diff > 0:
                pos_sum += diff
            elif diff < 0:
                neg_sum += diff
        
        if pos_sum + neg_sum != 0:
            return -1
        
        return pos_sum // k