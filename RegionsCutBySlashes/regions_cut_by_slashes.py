class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

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
            self.count -= 1
            return True
        return False

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        
        total_nodes = n * n * 4
        uf = UnionFind(total_nodes)

        for r in range(n):
            for c in range(n):
                cell_base_idx = 4 * (r * n + c)

                char = grid[r][c]
                if char == ' ':
                    uf.union(cell_base_idx + 0, cell_base_idx + 1)
                    uf.union(cell_base_idx + 1, cell_base_idx + 2)
                    uf.union(cell_base_idx + 2, cell_base_idx + 3)
                elif char == '/':
                    uf.union(cell_base_idx + 0, cell_base_idx + 3)
                    uf.union(cell_base_idx + 1, cell_base_idx + 2)
                elif char == '\\':
                    uf.union(cell_base_idx + 0, cell_base_idx + 1)
                    uf.union(cell_base_idx + 2, cell_base_idx + 3)
                
                if c + 1 < n:
                    current_cell_right_part = cell_base_idx + 1
                    right_cell_left_part = 4 * (r * n + (c + 1)) + 3
                    uf.union(current_cell_right_part, right_cell_left_part)
                
                if r + 1 < n:
                    current_cell_bottom_part = cell_base_idx + 2
                    bottom_cell_top_part = 4 * ((r + 1) * n + c) + 0
                    uf.union(current_cell_bottom_part, bottom_cell_top_part)
        
        return uf.count