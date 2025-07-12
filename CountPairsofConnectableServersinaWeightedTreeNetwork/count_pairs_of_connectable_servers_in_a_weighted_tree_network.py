import sys

sys.setrecursionlimit(2000)

class Solution:
    def countPairsOfConnectableServers(self, n: int, edges: list[list[int]], signalSpeed: int) -> list[int]:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        ans = [0] * n

        def dfs(u, parent, current_path_dist):
            count = 0
            if current_path_dist % signalSpeed == 0:
                count += 1

            for next_node, edge_w in adj[u]:
                if next_node != parent:
                    count += dfs(next_node, u, current_path_dist + edge_w)
            return count

        for c in range(n):
            total_valid_nodes_from_prev_subtrees = 0

            for neighbor, weight in adj[c]:
                count_valid_in_current_subtree = dfs(neighbor, c, weight)

                ans[c] += count_valid_in_current_subtree * total_valid_nodes_from_prev_subtrees

                total_valid_nodes_from_prev_subtrees += count_valid_in_current_subtree
        