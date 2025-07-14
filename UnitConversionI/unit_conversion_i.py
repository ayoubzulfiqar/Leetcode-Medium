import collections

class Solution:
    def baseUnitConversion(self, n: int, conversions: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7

        graph = [[] for _ in range(n)]
        for source, target, factor in conversions:
            graph[source].append((target, factor))

        baseUnitConversion = [-1] * n
        baseUnitConversion[0] = 1

        queue = collections.deque()
        queue.append(0)

        while queue:
            u = queue.popleft()

            for v, factor in graph[u]:
                if baseUnitConversion[v] == -1:
                    baseUnitConversion[v] = (baseUnitConversion[u] * factor) % MOD
                    queue.append(v)
        
        return baseUnitConversion