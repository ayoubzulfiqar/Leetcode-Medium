UNVISITED = 0
VISITING = 1
VISITED = 2

class Solution:
    def leadsToDestination(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)

        memo = [False] * n 
        state = [UNVISITED] * n

        def dfs(u: int) -> bool:
            if state[u] == VISITING:
                return False

            if state[u] == VISITED:
                return memo[u]

            state[u] = VISITING

            if not graph[u]:
                if u == destination:
                    memo[u] = True
                    state[u] = VISITED
                    return True
                else:
                    memo[u] = False
                    state[u] = VISITED
                    return False

            for v in graph[u]:
                if not dfs(v):
                    memo[u] = False
                    state[u] = VISITED
                    return False

            memo[u] = True
            state[u] = VISITED
            return True

        return dfs(source)