class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr: list[int]) -> bool:
        if not root:
            return False
        if not arr:
            return False

        def dfs(node, index):
            # If the current node is None, it means we've gone off the tree
            # This path is invalid.
            if not node:
                return False

            # If the current node's value does not match the expected value in the sequence
            # This path is invalid.
            if node.val != arr[index]:
                return False

            # If we have reached the end of the sequence (matched the last element)
            if index == len(arr) - 1:
                # For a valid sequence from root to leaves, the current node
                # MUST be a leaf node.
                return node.left is None and node.right is None

            # If we are not at the end of the sequence, continue searching in children.
            # The path is valid if it can be completed through the left child OR the right child.
            return dfs(node.left, index + 1) or dfs(node.right, index + 1)

        # Start the DFS from the root with the first element of the array (index 0)
        return dfs(root, 0)