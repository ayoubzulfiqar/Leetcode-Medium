class Solution:
    def canTransform(self, start: str, target: str) -> bool:
        n = len(start)
        i, j = 0, 0

        while i < n and j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1

            if i == n or j == n:
                break

            if start[i] != target[j]:
                return False

            if start[i] == 'L':
                if i < j:
                    return False
            elif start[i] == 'R':
                if i > j:
                    return False
            
            i += 1
            j += 1
        
        while i < n and start[i] == '_':
            i += 1
        while j < n and target[j] == '_':
            j += 1
        
        return i == n and j == n