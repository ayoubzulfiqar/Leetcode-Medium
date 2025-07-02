import collections

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = collections.defaultdict(dict)

        for i in range(len(equations)):
            A, B = equations[i]
            val = values[i]
            graph[A][B] = val
            graph[B][A] = 1.0 / val
        
        results = []
        
        for C, D in queries:
            ans = -1.0
            
            if C not in graph or D not in graph:
                ans = -1.0
            elif C == D:
                ans = 1.0
            else:
                queue = collections.deque([(C, 1.0)])
                visited = {C}
                
                while queue:
                    curr_node, curr_product = queue.popleft()
                    
                    if curr_node == D:
                        ans = curr_product
                        break
                    
                    for neighbor, weight in graph[curr_node].items():
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, curr_product * weight))
            
            results.append(ans)
            
        return results