from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first_misplaced: Optional[TreeNode] = None
        second_misplaced: Optional[TreeNode] = None
        prev_node: Optional[TreeNode] = None

        current: Optional[TreeNode] = root

        while current:
            if current.left is None:
                if prev_node and prev_node.val > current.val:
                    if first_misplaced is None:
                        first_misplaced = prev_node
                    second_misplaced = current
                prev_node = current
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    if prev_node and prev_node.val > current.val:
                        if first_misplaced is None:
                            first_misplaced = prev_node
                        second_misplaced = current
                    prev_node = current
                    current = current.right
        
        if first_misplaced and second_misplaced:
            first_misplaced.val, second_misplaced.val = second_misplaced.val, first_misplaced.val