import collections
import sys

sys.setrecursionlimit(10**5 + 100)

class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = [0] * n

        def dfs(node: int, parent: int) -> list[int]:
            counts = [0] * 26

            label_char_code = ord(labels[node]) - ord('a')
            counts[label_char_code] = 1

            for neighbor in adj[node]:
                if neighbor != parent:
                    child_counts = dfs(neighbor, node)
                    for i in range(26):
                        counts[i] += child_counts[i]
            
            ans[node] = counts[label_char_code]
            
            return counts

        dfs(0, -1)

        return ans