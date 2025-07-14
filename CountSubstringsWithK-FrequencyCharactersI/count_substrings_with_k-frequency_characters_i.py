import collections

class Solution:
    def countSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        total_count = 0

        for i in range(n):
            char_counts = collections.defaultdict(int)
            has_k_freq_char = False 

            for j in range(i, n):
                char = s[j]
                char_counts[char] += 1

                if char_counts[char] >= k:
                    has_k_freq_char = True 
                
                if has_k_freq_char:
                    total_count += 1
        
        return total_count