class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        in_degree = [0] * n

        for u, v in edges:
            in_degree[v] += 1

        champion = -1
        champion_count = 0

        for i in range(n):
            if in_degree[i] == 0:
                champion = i
                champion_count += 1
            
            if champion_count > 1:
                return -1
        
        return champion