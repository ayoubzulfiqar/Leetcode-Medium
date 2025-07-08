class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodesEqualSumDescendants(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            # Recursively get the total sum of values in the left subtree
            left_subtree_total_sum = dfs(node.left)
            
            # Recursively get the total sum of values in the right subtree
            right_subtree_total_sum = dfs(node.right)
            
            # The sum of descendants for the current node is the sum of its left and right subtrees
            sum_of_descendants = left_subtree_total_sum + right_subtree_total_sum
            
            # Check if the current node's value equals the sum of its descendants
            if node.val == sum_of_descendants:
                self.count += 1
            
            # Return the total sum of all nodes in the current subtree (including the current node's value)
            return node.val + left_subtree_total_sum + right_subtree_total_sum

        dfs(root)
        return self.count