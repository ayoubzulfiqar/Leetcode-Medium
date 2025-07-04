import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        
        diff_counts = count_t - count_s
        
        return sum(diff_counts.values())