class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_val):
            if not node:
                return 0

            current_val = current_val * 10 + node.val

            if not node.left and not node.right:
                return current_val
            
            return dfs(node.left, current_val) + dfs(node.right, current_val)
        
        return dfs(root, 0)