class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _insert_node(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self._insert_node(root.left, val)
        elif val > root.val:
            root.right = self._insert_node(root.right, val)
        # If val == root.val, we typically do nothing in a standard BST
        return root

    def _get_max_depth(self, node: TreeNode) -> int:
        if not node:
            return 0
        
        left_depth = self._get_max_depth(node.left)
        right_depth = self._get_max_depth(node.right)
        
        return 1 + max(left_depth, right_depth)

    def depthOfBST(self, insertion_order: list[int]) -> int:
        root = None
        for val in insertion_order:
            root = self._insert_node(root, val)
        
        return self._get_max_depth(root)