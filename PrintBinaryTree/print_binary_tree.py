import collections
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(root)

        m = height + 1
        n = (1 << (height + 1)) - 1

        res = [[""] * n for _ in range(m)]

        def place_node(node, r, c):
            if not node:
                return

            res[r][c] = str(node.val)

            offset = 1 << (height - r - 1)

            if node.left:
                place_node(node.left, r + 1, c - offset)

            if node.right:
                place_node(node.right, r + 1, c + offset)

        place_node(root, 0, (n - 1) // 2)

        return res