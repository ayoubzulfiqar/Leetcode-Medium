class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        if n > m:
            return self.isOneEditDistance(t, s)

        if m - n > 1:
            return False

        if n == m:
            diff_count = 0
            for i in range(n):
                if s[i] != t[i]:
                    diff_count += 1
            return diff_count == 1

        i = 0
        j = 0
        
        while i < n and s[i] == t[j]:
            i += 1
            j += 1
        
        if i == n:
            return True

        return s[i:] == t[j+1:]