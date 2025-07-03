class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return 0, None

            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)

            if left_height == right_height:
                return left_height + 1, node
            elif left_height > right_height:
                return left_height + 1, left_lca
            else:
                return right_height + 1, right_lca

        _, lca_node = dfs(root)
        return lca_node