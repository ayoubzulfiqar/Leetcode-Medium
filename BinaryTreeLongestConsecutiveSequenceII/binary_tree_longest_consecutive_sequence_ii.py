class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_len = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_len = 0 
        self._dfs(root)
        return self.max_len

    def _dfs(self, node):
        if not node:
            return 0, 0 # (longest_increasing_path_ending_at_node, longest_decreasing_path_ending_at_node)

        current_inc = 1 # Length of increasing path starting at node (at least node itself)
        current_dec = 1 # Length of decreasing path starting at node (at least node itself)

        left_inc, left_dec = self._dfs(node.left)
        right_inc, right_dec = self._dfs(node.right)

        # Calculate longest increasing path starting at 'node' and going down
        if node.left:
            if node.left.val == node.val + 1:
                current_inc = max(current_inc, 1 + left_inc)
            elif node.left.val == node.val - 1:
                current_dec = max(current_dec, 1 + left_dec)
        
        if node.right:
            if node.right.val == node.val + 1:
                current_inc = max(current_inc, 1 + right_inc)