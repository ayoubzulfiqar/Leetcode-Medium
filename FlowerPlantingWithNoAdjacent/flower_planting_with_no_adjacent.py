import collections

class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        graph = collections.defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)

        ans = [0] * n

        for i in range(1, n + 1):
            used_flowers = set()
            
            for neighbor in graph[i]:
                if ans[neighbor - 1] != 0:
                    used_flowers.add(ans[neighbor - 1])
            
            for flower_type in range(1, 5):
                if flower_type not in used_flowers:
                    ans[i - 1] = flower_type
                    break

        return ans