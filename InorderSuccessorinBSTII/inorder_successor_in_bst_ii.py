class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Case 1: If the node has a right child, the successor is the leftmost node in its right subtree.
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current
        
        # Case 2: If the node does not have a right child, the successor is one of its ancestors.
        # We go up using the parent pointer until we find an ancestor that is greater than the current node.
        # This happens when we move up from a left child to its parent.
        current = node
        while current.parent and current == current.parent.right:
            current = current.parent
        
        # If current.parent is None, it means we have reached the root and the original node
        # was the largest element in the BST, so it has no inorder successor.
        return current.parent