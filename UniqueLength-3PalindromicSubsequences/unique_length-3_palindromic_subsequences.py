class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        count = 0
        
        first_occurrence = [-1] * 26
        last_occurrence = [-1] * 26
        
        n = len(s)
        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            if first_occurrence[char_idx] == -1:
                first_occurrence[char_idx] = i
            last_occurrence[char_idx] = i
            
        for i in range(26):
            first_idx = first_occurrence[i]
            last_idx = last_occurrence[i]
            
            if first_idx != -1 and first_idx < last_idx:
                middle_chars = set()
                for j in range(first_idx + 1, last_idx):
                    middle_chars.add(s[j])
                
                count += len(middle_chars)
                
        return count