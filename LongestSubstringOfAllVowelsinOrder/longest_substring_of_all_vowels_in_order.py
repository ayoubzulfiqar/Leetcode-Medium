class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        max_length = 0
        current_length = 0
        vowels_in_current_substring = set()
        last_char = ''

        for char in word:
            if char >= last_char:
                current_length += 1
                vowels_in_current_substring.add(char)
            else:
                current_length = 1
                vowels_in_current_substring = {char}
            
            last_char = char
            
            if len(vowels_in_current_substring) == 5:
                max_length = max(max_length, current_length)
                
        return max_length