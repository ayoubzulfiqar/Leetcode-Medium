class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        MOD = 10**9 + 7

        def calculate_total_sum(node):
            if not node:
                return 0
            return node.val + calculate_total_sum(node.left) + calculate_total_sum(node.right)

        total_sum = calculate_total_sum(root)
        
        max_product = 0

        def dfs_find_max_product(node):
            nonlocal max_product
            nonlocal total_sum

            if not node:
                return 0
            
            left_subtree_sum = dfs_find_max_product(node.left)
            right_subtree_sum = dfs_find_max_product(node.right)
            
            current_subtree_sum = node.val + left_subtree_sum + right_subtree_sum
            
            max_product = max(max_product, current_subtree_sum * (total_sum - current_subtree_sum))
            
            return current_subtree_sum

        dfs_find_max_product(root)
        
        return max_product % MOD