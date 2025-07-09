import collections

class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        
        component_sizes = []

        for i in range(n):
            if not visited[i]:
                current_component_size = 0
                q = collections.deque([i])
                visited[i] = True
                
                while q:
                    node = q.popleft()
                    current_component_size += 1
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                component_sizes.append(current_component_size)
        
        sum_of_squares_of_component_sizes = 0
        for size in component_sizes:
            sum_of_squares_of_component_sizes += size * size
        
        return (n * n - sum_of_squares_of_component_sizes) // 2