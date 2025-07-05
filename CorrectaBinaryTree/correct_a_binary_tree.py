class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        This solution assumes the problem refers to "Recover Binary Search Tree",
        where exactly two nodes in a BST have been swapped.
        """
        
        # Pointers to store the two swapped nodes
        self.first_node = None
        self.second_node = None
        
        # Pointer to store the previously visited node in in-order traversal
        self.prev_node = None
        
        def inorder_traverse(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder_traverse(node.left)
            
            # Process current node
            # Check for violation: if current node's value is less than previous node's value
            if self.prev_node and node.val < self.prev_node.val:
                # If this is the first violation, prev_node is the first swapped node
                if not self.first_node:
                    self.first_node = self.prev_node
                # The current node is always the second swapped node (or the second part of the first violation)
                self.second_node = node
            
            # Update prev_node for the next comparison
            self.prev_node = node
            
            # Traverse right subtree
            inorder_traverse(node.right)
            
        inorder_traverse(root)
        
        # Swap the values of the two identified nodes
        if self.first_node and self.second_node:
            self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val