class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        max_length = 0
        char_counts = {}

        for right in range(len(s)):
            char = s[right]
            char_counts[char] = char_counts.get(char, 0) + 1

            while len(char_counts) > 2:
                left_char = s[left]
                char_counts[left_char] -= 1
                if char_counts[left_char] == 0:
                    del char_counts[left_char]
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length