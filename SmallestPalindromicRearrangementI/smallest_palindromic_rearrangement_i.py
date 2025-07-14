import collections

class Solution:
    def smallestPalindromicRearrangement(self, s: str) -> str:
        char_counts = collections.Counter(s)
        
        first_half_chars = []
        middle_char = ""
        
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            count = char_counts[char]
            
            if count == 0:
                continue
                
            if count % 2 == 1:
                middle_char = char
                first_half_chars.extend([char] * ((count - 1) // 2))
            else:
                first_half_chars.extend([char] * (count // 2))
                
        first_half_str = "".join(first_half_chars)
        
        return first_half_str + middle_char + first_half_str[::-1]