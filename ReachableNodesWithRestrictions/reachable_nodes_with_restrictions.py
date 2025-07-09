import collections

class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        restricted_set = set(restricted)

        q = collections.deque()
        visited = set()
        reachable_count = 0

        # Node 0 is guaranteed not to be restricted
        q.append(0)
        visited.add(0)
        reachable_count = 1

        while q:
            curr_node = q.popleft()

            for neighbor in adj[curr_node]:
                if neighbor not in visited and neighbor not in restricted_set:
                    visited.add(neighbor)
                    q.append(neighbor)
                    reachable_count += 1

        return reachable_count