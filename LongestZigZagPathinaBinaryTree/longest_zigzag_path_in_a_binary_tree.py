class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_len = 0

        def dfs(node):
            if not node:
                return (-1, -1)

            left_path_from_left_child, right_path_from_left_child = dfs(node.left)
            left_path_from_right_child, right_path_from_right_child = dfs(node.right)

            current_path_going_right = 1 + left_path_from_right_child
            current_path_going_left = 1 + right_path_from_left_child

            self.max_len = max(self.max_len, current_path_going_left, current_path_going_right)

            return (current_path_going_left, current_path_going_right)

        dfs(root)
        return self.max_len