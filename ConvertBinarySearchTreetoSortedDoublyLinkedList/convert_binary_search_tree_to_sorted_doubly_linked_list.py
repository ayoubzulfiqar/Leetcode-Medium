class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        head = None
        prev = None

        def inorder_traverse(node):
            nonlocal head, prev

            if not node:
                return

            inorder_traverse(node.left)

            if prev:
                prev.right = node
                node.left = prev
            else:
                head = node

            prev = node

            inorder_traverse(node.right)

        inorder_traverse(root)

        if head and prev:
            head.left = prev
            prev.right = head

        return head