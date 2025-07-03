import collections

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        # color[i] = 0: uncolored
        # color[i] = 1: group A
        # color[i] = -1: group B
        color = [0] * (n + 1)

        for i in range(1, n + 1):
            if color[i] == 0:  # If person i is not yet colored
                q = collections.deque()
                q.append(i)
                color[i] = 1  # Assign person i to group A

                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if color[v] == 0:  # If neighbor v is uncolored
                            color[v] = -color[u]  # Assign v to the opposite group of u
                            q.append(v)
                        elif color[v] == color[u]:  # If neighbor v has the same color as u
                            return False  # Conflict found, not bipartite

        return True