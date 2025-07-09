import collections

class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        rev_adj = [[] for _ in range(n)]
        for fromi, toi in edges:
            rev_adj[toi].append(fromi)
        
        ancestors = [set() for _ in range(n)]
        
        for i in range(n):
            q = collections.deque()
            q.append(i)
            
            visited = {i} 
            
            while q:
                curr = q.popleft()
                
                for prev_node in rev_adj[curr]:
                    if prev_node not in visited:
                        visited.add(prev_node)
                        ancestors[i].add(prev_node)
                        q.append(prev_node)
        
        result = []
        for i in range(n):
            result.append(sorted(list(ancestors[i])))
            
        return result