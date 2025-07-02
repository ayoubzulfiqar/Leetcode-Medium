class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_length = 0

        def dfs(node):
            if not node:
                return 0

            left_path_len = dfs(node.left)
            right_path_len = dfs(node.right)

            current_left_len = 0
            current_right_len = 0

            if node.left and node.left.val == node.val:
                current_left_len = 1 + left_path_len
            
            if node.right and node.right.val == node.val:
                current_right_len = 1 + right_path_len
            
            self.max_length = max(self.max_length, current_left_len + current_right_len)
            
            return max(current_left_len, current_right_len)
        
        dfs(root)
        return self.max_length