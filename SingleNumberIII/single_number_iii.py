class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        diff_bit = xor_sum & (-xor_sum)
        
        single1 = 0
        single2 = 0
        
        for num in nums:
            if (num & diff_bit) == 0:
                single1 ^= num
            else:
                single2 ^= num
                
        return [single1, single2]