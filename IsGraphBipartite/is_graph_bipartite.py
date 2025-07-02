from collections import deque

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        colors = [0] * n  # 0: uncolored, 1: color A, -1: color B

        for i in range(n):
            if colors[i] == 0:  # If node i is uncolored, start BFS from it
                queue = deque()
                queue.append(i)
                colors[i] = 1  # Assign color A to the starting node of this component

                while queue:
                    u = queue.popleft()

                    for v in graph[u]:
                        if colors[v] == 0:  # If neighbor v is uncolored
                            colors[v] = -colors[u]  # Assign opposite color
                            queue.append(v)
                        elif colors[v] == colors[u]:  # If neighbor v has the same color as u
                            return False  # Not bipartite, conflict found

        return True