import collections

class Solution:
    def maximizeTheNumberOfTargetNodes(self, n: int, edges1: list[list[int]], m: int, edges2: list[list[int]], k: int) -> list[int]:
        def bfs(start_node: int, num_nodes: int, adj: list[list[int]]) -> list[int]:
            distances = [-1] * num_nodes
            distances[start_node] = 0
            queue = collections.deque([start_node])

            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if distances[v] == -1:
                        distances[v] = distances[u] + 1
                        queue.append(v)
            return distances

        adj1 = [[] for _ in range(n)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        adj2 = [[] for _ in range(m)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        dist1 = []
        for i in range(n):
            dist1.append(bfs(i, n, adj1))

        dist2 = []
        for j in range(m):
            dist2.append(bfs(j, m, adj2))

        count1 = [0] * n
        for i in range(n):
            for x in range(n):
                if dist1[i][x] != -1 and dist1[i][x] <= k:
                    count1[i] += 1

        count2_prefix = [0] * m
        for j in range(m):
            for y in range(m):
                if dist2[j][y] != -1 and dist2[j][y] <= k - 1:
                    count2_prefix[j] += 1

        answer = [0] * n
        for i in range(n):
            max_for_i = 0
            for j in range(m):
                current_total = count1[i] + count2_prefix[j]
                max_for_i = max(max_for_i, current_total)
            answer[i] = max_for_i

        return answer