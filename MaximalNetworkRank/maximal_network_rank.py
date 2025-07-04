class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        adj = [set() for _ in range(n)]
        degree = [0] * n

        for u, v in roads:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1

        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                current_rank = degree[i] + degree[j]
                if j in adj[i]:
                    current_rank -= 1
                max_rank = max(max_rank, current_rank)
        
        return max_rank