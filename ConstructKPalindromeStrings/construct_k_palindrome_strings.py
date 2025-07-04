import collections

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        char_counts = collections.Counter(s)
        odd_counts = 0
        for count in char_counts.values():
            if count % 2 != 0:
                odd_counts += 1

        if k < odd_counts:
            return False
            
        return True