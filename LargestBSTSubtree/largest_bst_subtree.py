from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_bst_size = 0

        # Helper function performs a post-order traversal (DFS)
        # and returns a tuple: (is_bst, size, min_val, max_val)
        # - is_bst: True if the subtree rooted at 'node' is a BST, False otherwise.
        # - size: The number of nodes in the subtree if it's a BST, otherwise 0 (or arbitrary).
        # - min_val: The minimum value in the subtree.
        # - max_val: The maximum value in the subtree.
        def dfs(node: Optional[TreeNode]):
            # Base case: An empty tree is considered a BST of size 0.
            # We use math.inf and -math.inf for min/max to ensure comparisons with parent nodes work correctly.
            # For a left child, its max_val should be less than parent.val.
            # For a right child, its min_val should be greater than parent.val.
            if not node:
                return True, 0, math.inf, -math.inf

            # Recursively get information from the left and right children
            left_is_bst, left_size, left_min, left_max = dfs(node.left)
            right_is_bst, right_size, right_min, right_max = dfs(node.right)

            # Check if the current subtree rooted at 'node' is a BST:
            # 1. Both left and right subtrees must themselves be BSTs.
            # 2. The current node's value must be greater than the maximum value in its left subtree.
            # 3. The current node's value must be less than the minimum value in its right subtree.
            if left_is_bst and right_is_bst and \
               node.val > left_max and node.val < right_min:
                
                # If all conditions are met, this subtree is a BST.
                current_size = 1 + left_size + right_size
                
                # Update the global maximum BST size found so far.
                self.max_bst_size = max(self.max_bst_size, current_size)
                
                # Calculate the true minimum and maximum values for this valid BST subtree.
                # If left_child was None, left_min is math.inf, so min(node.val, math.inf) correctly yields node.val.
                # If right_child was None, right_max is -math.inf, so max(node.val, -math.inf) correctly yields node.val.
                current_min = min(node.val, left_min) 
                current_max = max(node.val, right_max)
                
                return True, current_size, current_min, current_max
            else:
                # If any condition fails, this subtree is NOT a BST.
                # We signal this by returning False for 'is_bst'.
                # The other returned values (size, min, max) are arbitrary/dummy
                # because this subtree itself is not a valid BST.
                # The 'max_bst_size' will have been updated by any valid BSTs found deeper in the tree.
                return False, 0, 0, 0

        # Initiate the DFS traversal from the root of the entire tree.
        dfs(root)
        
        # After the traversal, self.max_bst_size will hold the size of the largest BST subtree found.
        return self.max_bst_size