class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        n = len(stones)
        
        parent = list(range(n))
        
        size = [1] * n 
        
        num_components = n
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            nonlocal num_components
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i 
                
                parent[root_j] = root_i
                size[root_i] += size[root_j]
                num_components -= 1
                return True
            return False

        row_map = {} 
        col_map = {} 
        
        for i in range(n):
            x, y = stones[i]
            row_map.setdefault(x, []).append(i)
            col_map.setdefault(y, []).append(i)
            
        for row_val in row_map:
            indices = row_map[row_val]
            if len(indices) > 1:
                for k in range(1, len(indices)):
                    union(indices[0], indices[k])
                    
        for col_val in col_map:
            indices = col_map[col_val]
            if len(indices) > 1:
                for k in range(1, len(indices)):
                    union(indices[0], indices[k])
        
        return n - num_components