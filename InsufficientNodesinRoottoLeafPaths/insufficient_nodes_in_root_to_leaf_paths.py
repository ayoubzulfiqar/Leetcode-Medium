class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        
        def dfs(node, current_path_sum):
            if not node:
                return False

            current_path_