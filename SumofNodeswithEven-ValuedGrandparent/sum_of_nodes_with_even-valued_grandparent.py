class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total_sum = 0

        def dfs(node, parent_val, grandparent_val):
            nonlocal total_sum
            if not node:
                return

            if grandparent_val % 2 == 0:
                total_sum += node.val

            dfs(node.left, node.val, parent_val)
            dfs(node.right, node.val, parent_val)

        dfs(root, 1, 1)

        return total_sum