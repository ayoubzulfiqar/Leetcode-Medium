class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_length = 1
        current_length = 1

        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                current_length += 1
            else:
                current_length = 1
            max_length = max(max_length, current_length)

        return max_length