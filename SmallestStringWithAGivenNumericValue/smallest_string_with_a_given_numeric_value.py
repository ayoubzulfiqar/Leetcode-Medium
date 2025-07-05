class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = [''] * n
        
        for i in range(n - 1, -1, -1):
            remaining_len_for_as = i
            
            char_val = min(26, k - remaining_len_for_as)
            
            result[i] = chr(ord('a') + char_val - 1)
            
            k -= char_val
            
        return "".join(result)