import collections

class Solution:
    def numberOfEqualCountSubstrings(self, s: str) -> int:
        n = len(s)
        total_count = 0

        for i in range(n):
            char_counts = [0] * 26 
            
            for j in range(i, n):
                char_counts[ord(s[j]) - ord('a')] += 1
                
                first_freq = -1
                is_equal_count = True
                
                for k in range(26):
                    current_char_freq = char_counts[k]
                    
                    if current_char_freq > 0:
                        if first_freq == -1:
                            first_freq = current_char_freq
                        elif current_char_freq != first_freq:
                            is_equal_count = False
                            break
                
                if is_equal_count:
                    total_count += 1
        
        return total_count