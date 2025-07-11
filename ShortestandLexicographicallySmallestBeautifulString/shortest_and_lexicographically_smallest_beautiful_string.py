import sys

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        min_len = sys.maxsize
        
        for i in range(n):
            current_ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    current_ones += 1
                
                if current_ones == k:
                    current_len = j - i + 1
                    min_len = min(min_len, current_len)
                    break 
        
        if min_len == sys.maxsize:
            return ""
        
        ans = "~" 
        
        for i in range(n):
            current_ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    current_ones += 1
                
                current_len = j - i + 1
                
                if current_len > min_len:
                    break 
                
                if current_ones == k and current_len == min_len:
                    sub = s[i : j+1]
                    if sub < ans:
                        ans = sub
                    break 
                    
        return ans