import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        
        factorials = [1] * (n + 1)
        for i in range(2, n + 1):
            factorials[i] = factorials[i-1] * i
        
        result = []
        k -= 1 
        
        for i in range(n - 1, -1, -1):
            block_size = factorials[i] 
            
            idx = k // block_size
            
            result.append(nums[idx])
            
            nums.pop(idx)
            
            k %= block_size
            
        return "".join(result)