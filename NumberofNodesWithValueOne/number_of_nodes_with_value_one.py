class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def count_nodes_with_value_one(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        if root.val == 1:
            count += 1

        count += self.count_nodes_with_value_one(root.left)
        count += self.count_nodes_with_value_one(root.right)

        return count