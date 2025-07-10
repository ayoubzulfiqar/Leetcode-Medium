class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        count = 0
        current_xor_sum = 0
        freq = {0: 1} 

        for num in nums:
            current_xor_sum ^= num
            if current_xor_sum in freq:
                count += freq[current_xor_sum]
                freq[current_xor_sum] += 1
            else:
                freq[current_xor_sum] = 1
        
        return count