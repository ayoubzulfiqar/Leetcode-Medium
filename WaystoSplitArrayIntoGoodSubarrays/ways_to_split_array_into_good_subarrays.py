class Solution:
    def numberOfGoodSubarraySplits(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        one_indices = []
        for i, num in enumerate(nums):
            if num == 1:
                one_indices.append(i)
        
        if not one_indices:
            return 0
        
        ways = 1
        
        for i in range(len(one_indices) - 1):
            gap_length = one_indices[i+1] - one_indices[i]
            ways = (ways * gap_length) % MOD
            
        return ways