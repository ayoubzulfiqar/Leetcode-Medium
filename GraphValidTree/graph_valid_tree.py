class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False
        
        if self.size[root_i] < self.size[root_j]:
            root_i, root_j = root_j, root_i

        self.parent[root_j] = root_i
        self.size[root_i] += self.size[root_j]
        return True

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        
        for u, v in edges:
            if not uf.union(u, v):
                return False
        
        return True