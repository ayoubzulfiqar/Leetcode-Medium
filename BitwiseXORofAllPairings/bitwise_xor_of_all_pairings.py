class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        xor_sum1 = 0
        for num in nums1:
            xor_sum1 ^= num

        xor_sum2 = 0
        for num in nums2:
            xor_sum2 ^= num

        result = 0
        
        # If the length of nums2 (m) is odd, each element of nums1 contributes
        # itself to the final XOR sum. This is because each nums1[i] is XORed
        # with all m elements of nums2. When m is odd, nums1[i] appears an odd
        # number of times (m times) in the expanded sum for each nums1[i],
        # effectively keeping its value.
        if m % 2 == 1:
            result ^= xor_sum1
        
        # Similarly, if the length of nums1 (n) is odd, each element of nums2
        # contributes itself to the final XOR sum.
        if n % 2 == 1:
            result ^= xor_sum2
            
        return result