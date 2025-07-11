class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        current_xor_sum = 0
        for num in nums:
            current_xor_sum ^= num
        
        diff_xor = current_xor_sum ^ k
        
        return diff_xor.bit_count()