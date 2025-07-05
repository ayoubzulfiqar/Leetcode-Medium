class Solution:
    def countDistinctSubstrings(self, s: str) -> int:
        distinct_substrings = set()
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                distinct_substrings.add(substring)
        return len(distinct_substrings)