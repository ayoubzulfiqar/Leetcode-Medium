class Solution:
    def isSubsequence(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1
        return i == len(s1)

    def findLUSlength(self, strs: list[str]) -> int:
        max_len = -1
        n = len(strs)

        for i in range(n):
            is_uncommon = True
            for j in range(n):
                if i == j:
                    continue
                if self.isSubsequence(strs[i], strs[j]):
                    is_uncommon = False
                    break
            
            if is_uncommon:
                max_len = max(max_len, len(strs[i]))
        
        return max_len