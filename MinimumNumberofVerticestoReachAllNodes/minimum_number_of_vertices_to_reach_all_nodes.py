class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        in_degree = [0] * n

        for _, to_node in edges:
            in_degree[to_node] += 1

        result = []
        for i in range(n):
            if in_degree[i] == 0:
                result.append(i)
        
        return result