class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        xor_sum = 0
        for val in derived:
            xor_sum ^= val
        
        return xor_sum == 0