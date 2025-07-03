class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        deleted_count = 0
        sorted_pairs = [False] * (n - 1)

        for j in range(m):
            can_keep_column = True
            
            for i in range(n - 1):
                if not sorted_pairs[i]:
                    if strs[i][j] > strs[i+1][j]:
                        can_keep_column = False
                        deleted_count += 1
                        break
            
            if can_keep_column:
                for i in range(n - 1):
                    if not sorted_pairs[i]:
                        if strs[i][j] < strs[i+1][j]:
                            sorted_pairs[i] = True
        
        return deleted_count