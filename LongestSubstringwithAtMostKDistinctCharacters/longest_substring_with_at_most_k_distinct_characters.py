import collections

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        n = len(s)
        if n == 0:
            return 0
        
        char_counts = collections.defaultdict(int)
        
        left = 0
        max_len = 0
        
        for right in range(n):
            char_counts[s[right]] += 1
            
            while len(char_counts) > k:
                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 0:
                    del char_counts[s[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len