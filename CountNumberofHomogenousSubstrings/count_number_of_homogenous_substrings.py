class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        total_count = 0
        n = len(s)
        
        if n == 0:
            return 0

        current_length = 0
        
        for i in range(n):
            if i == 0 or s[i] == s[i-1]:
                current_length += 1
            else:
                total_count = (total_count + (current_length * (current_length + 1) // 2)) % MOD
                current_length = 1
        
        total_count = (total_count + (current_length * (current_length + 1) // 2)) % MOD
        
        return total_count