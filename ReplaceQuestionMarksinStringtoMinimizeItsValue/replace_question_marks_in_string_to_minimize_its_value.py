class Solution:
    def minimizeStringValue(self, s: str) -> str:
        n = len(s)
        result_chars = list(s)
        
        counts = [0] * 26 
        
        for i in range(n):
            if result_chars[i] == '?':
                min_count = float('inf')
                best_char_code = -1
                
                for j in range(26):
                    if counts[j] < min_count:
                        min_count = counts[j]
                        best_char_code = j
                
                result_chars[i] = chr(ord('a') + best_char_code)
                counts[best_char_code] += 1
            else:
                char_code = ord(result_chars[i]) - ord('a')
                counts[char_code] += 1
                
        return "".join(result_chars)