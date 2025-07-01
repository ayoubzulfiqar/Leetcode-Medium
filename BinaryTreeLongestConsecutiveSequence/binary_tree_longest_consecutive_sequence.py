class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_len = 0

        def dfs(node):
            if not node:
                return 0

            current_node_path_length = 1
            
            left_sequence_length = dfs(node.left)
            if node.left and node.left.val == node.val + 1:
                current_node_path_length = max(current_node_path_length, 1 + left_sequence_length)
            
            right_sequence_length = dfs(node.right)
            if node.right and node.right.val == node.val + 1:
                current_node_path_length = max(current_node_path_length, 1 + right_sequence_length)
            
            self.max_len = max(self.max_len, current_node_path_length)
            
            return current_node_path_length

        dfs(root)
        
        return self.max_len