class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_j] < rank[root_i]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                return True
            return False

        connections.sort(key=lambda x: x[2])

        total_cost = 0
        edges_count = 0

        for u, v, cost in connections:
            if union(u, v):
                total_cost += cost
                edges_count += 1
                if edges_count == n - 1:
                    return total_cost
        
        return total_cost if edges_count == n - 1 else -1