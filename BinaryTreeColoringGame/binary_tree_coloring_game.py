class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningStrategy(self, root: TreeNode, n: int, x: int) -> bool:
        self.left_subtree_of_x_size = 0
        self.right_subtree_of_x_size = 0

        def dfs_calculate_sizes(node):
            if not node:
                return 0

            left_count = dfs_calculate_sizes(node.left)
            right_count = dfs_calculate_sizes(node.right)

            if node.val == x:
                self.left_subtree_of_x_size = left_count
                self.right_subtree_of_x_size = right_count
            
            return 1 + left_count + right_count

        dfs_calculate_sizes(root)

        parent_side_size = n - (1 + self.left_subtree_of_x_size + self.right_subtree_of_x_size)

        if self.left_subtree_of_x_size > n // 2:
            return True
        
        if self.right_subtree_of_x_size > n // 2:
            return True
        
        if parent_side_size > n // 2:
            return True
        
        return False