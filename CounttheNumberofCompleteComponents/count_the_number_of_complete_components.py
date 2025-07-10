import collections

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        visited = [False] * n
        complete_components_count = 0

        for i in range(n):
            if not visited[i]:
                current_component_nodes_list = []
                
                bfs_q = collections.deque([i])
                visited[i] = True
                current_component_nodes_list.append(i)

                while bfs_q:
                    u = bfs_q.popleft()
                    
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            bfs_q.append(v)
                            current_component_nodes_list.append(v)
                
                num_nodes_in_component = len(current_