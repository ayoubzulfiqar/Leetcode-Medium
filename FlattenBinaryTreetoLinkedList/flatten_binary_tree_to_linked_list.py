class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node in the left subtree
                # This node will become the new parent of curr.right
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # Connect the rightmost node of the left subtree to the original right subtree
                predecessor.right = curr.right
                
                # Move the left subtree to the right of the current node
                curr.right = curr.left
                
                # Set the left child to None
                curr.left = None
            
            # Move to the next node in the flattened list (which is now curr.right)
            curr = curr.right