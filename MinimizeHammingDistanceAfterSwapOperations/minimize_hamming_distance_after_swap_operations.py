import collections

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

class Solution:
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        n = len(source)
        dsu = DSU(n)

        for u, v in allowedSwaps:
            dsu.union(u, v)

        component_groups = collections.defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            component_groups[root].append(i)

        total_matches = 0
        for indices_in_component in component_groups.values():
            source_counts = collections.defaultdict(int)
            target_counts = collections.defaultdict(int)

            for idx in indices_in_component:
                source_counts[source[idx]] += 1
                target_counts[target[idx]] += 1

            for val, count in source_counts.items():
                if val in target_counts:
                    total_matches += min(count, target_counts[val])

        return n - total_matches