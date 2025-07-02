import collections

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self._longestSubstring(s, 0, len(s), k)

    def _longestSubstring(self, s: str, start: int, end: int, k: int) -> int:
        if end - start