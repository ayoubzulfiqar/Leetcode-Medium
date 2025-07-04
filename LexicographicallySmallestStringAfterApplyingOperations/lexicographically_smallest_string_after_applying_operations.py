import collections

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        
        q = collections.deque()
        q.append(s)
        
        visited = {s}
        
        smallest_string = s
        
        while q:
            curr_s = q.popleft()
            
            if curr_s < smallest_string:
                smallest_string = curr_s
            
            s_list = list(curr_s)
            for i in range(1, n, 2):
                s_list[i] = str((int(s_list[i]) + a) % 10)
            next_s_add = "".join(s_list)
            
            if next_s_add not in visited:
                visited.add(next_s_add)
                q.append(next_s_add)
                
            next_s_rotate = curr_s[-b:] + curr_s[:-b]
            
            if next_s_rotate not in visited:
                visited.add(next_s_rotate)
                q.append(next_s_rotate)
                
        return smallest_string