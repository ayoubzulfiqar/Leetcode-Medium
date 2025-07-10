class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        count = 0
        left = 0
        seen_chars = set()

        for right in range(n):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            
            seen_chars.add(s[right])
            
            count += (right - left + 1)
            
        return count