class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) < 2:
            return s

        start = 0
        max_len = 1

        def expand_around_center(left, right):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            current_len = right - (left + 1)
            if current_len > max_len:
                max_len = current_len
                start = left + 1

        for i in range(len(s)):
            expand_around_center(i, i)
            expand_around_center(i, i + 1)

        return s[start : start + max_len]