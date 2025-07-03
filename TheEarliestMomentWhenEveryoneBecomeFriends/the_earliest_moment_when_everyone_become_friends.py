class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_j] < self.rank[root_i]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            self.num_components -= 1
            return True
        return False

class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])

        uf = UnionFind(n)

        if n == 1:
            return 0

        for timestamp, personA, personB in logs:
            uf.union(personA, personB)
            if uf.num_components == 1:
                return timestamp

        return -1