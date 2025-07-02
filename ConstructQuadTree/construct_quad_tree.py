class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        n = len(grid)

        def build_tree(r_start, c_start, size):
            first_val = grid[r_start][c_start]
            all_same = True
            for r in range(r_start, r_start + size):
                for c in range(c_start, c_start + size):
                    if grid[r][c] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break

            if all_same:
                return Node(val=bool(first_val), isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            else:
                node = Node(val=True, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
                
                new_size = size // 2
                node.topLeft = build_tree(r_start, c_start, new_size)
                node.topRight = build_tree(r_start, c_start + new_size, new_size)
                node.bottomLeft = build_tree(r_start + new_size, c_start, new_size)
                node.bottomRight = build_tree(r_start + new_size, c_start + new_size, new_size)
                
                return node

        return build_tree(0, 0, n)