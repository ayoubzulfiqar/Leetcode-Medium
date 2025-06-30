class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        
        for i in range(32):
            bit_sum = 0
            for num in nums:
                if (num >> i) & 1:
                    bit_sum += 1
            
            if bit_sum % 3 == 1:
                result |= (1 << i)
        
        if (result & (1 << 31)) != 0:
            result = result - (1 << 32)
            
        return result