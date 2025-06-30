class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        if root.left:
            # Connect left child to right child (siblings)
            root.left.next = root.right

            # Connect right child to the left child of the next node in the same level
            # This is only possible if root.next exists
            if root.next:
                root.right.next = root.next.left

        # Recursively call for left and right subtrees
        self.connect(root.left)
        self.connect(root.right)

        return root