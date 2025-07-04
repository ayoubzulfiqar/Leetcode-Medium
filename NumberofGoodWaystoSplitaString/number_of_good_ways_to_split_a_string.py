class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        
        left_distinct = [0] * n
        current_set = set()
        for i in range(n):
            current_set.add(s[i])
            left_distinct[i] = len(current_set)
            
        right_distinct = [0] * n
        current_set = set()
        for i in range(n - 1, -1, -1):
            current_set.add(s[i])
            right_distinct[i] = len(current_set)
            
        good_splits = 0
        for i in range(n - 1):
            if left_distinct[i] == right_distinct[i+1]:
                good_splits += 1
                
        return good_splits