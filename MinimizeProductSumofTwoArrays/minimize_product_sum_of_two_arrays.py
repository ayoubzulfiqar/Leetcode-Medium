class Solution:
    def minProductSum(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        
        min_product_sum = 0
        for i in range(len(nums1)):
            min_product_sum += nums1[i] * nums2[i]
            
        return min_product_sum