import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = [root.val]

        # Handle single node tree
        if not root.left and not root.right:
            return result

        # 1. Left Boundary (excluding root and leaf)
        curr = root.left
        while curr:
            if curr.left or curr.right: # Not a leaf
                result.append(curr.val)
            else: # It's a leaf, will be handled by leaf traversal
                break
            
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        # 2. Leaves (left to right)
        # Use a DFS helper
        leaves = []
        def find_leaves(node):
            if not node:
                return
            if not node.left and not node.right: # Is a leaf
                leaves.append(node.val)
                return
            find_leaves(node.left)
            find_leaves(node.right)
        
        find_leaves(root)
        result.extend(leaves)

        # 3. Right Boundary (excluding root and leaf, in reverse order)
        right_boundary_nodes = []
        curr = root.right
        while curr:
            if curr.left or curr.right: # Not a leaf
                right_boundary_nodes.append(curr.val)
            else: # It's a leaf, already handled by leaf traversal
                break
            
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        
        result.extend(right_boundary_nodes[::-1])

        return result