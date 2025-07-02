class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node, current_depth):
            if not node:
                return

            if current_depth == depth - 1:
                original_left = node.left
                new_left_node = TreeNode(val)
                new_left_node.left = original_left
                node.left = new_left_node

                original_right = node.right
                new_right_node = TreeNode(val)
                new_right_node.right = original_right
                node.right = new_right_node
                return

            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)

        dfs(root, 1)
        return root