class Solution:
    def solve(self, properties: list[list[int]], k: int) -> int:
        n = len(properties)
        
        # DSU initialization
        parent = list(range(n))
        num_components = n

        # Helper function for DSU find operation with path compression
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        # Helper function for DSU union operation
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_j] = root_i
                nonlocal num_components
                num_components -= 1
                return True
            return False

        # Helper function to calculate the number of distinct common integers
        def intersect(arr1, arr2):
            set1 = set(arr1)
            set2 = set(arr2)
            return len(set1.intersection(set2))

        # Iterate through all unique pairs of properties to build edges
        for i in range(n):
            for j in range(i + 1, n):
                if intersect(properties[i], properties[j]) >= k:
                    union(i, j)
        
        return num_components