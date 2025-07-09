import collections

class Solution:
    def countSubstrings(self, s: str) -> int:
        char_counts = collections.Counter(s)
        total_substrings = 0
        for count in char_counts.values():
            total_substrings += count * (count + 1) // 2
        return total_substrings