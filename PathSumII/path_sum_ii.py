# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        results = []
        current_path = []

        def dfs(node, remaining_sum):
            if not node:
                return

            current_path.append(node.val)
            remaining_sum -= node.val

            # Check if it's a leaf node and the sum matches
            if not node.left and not node.right and remaining_sum == 0:
                results.append(list(current_path))

            # Recurse on left and right children
            dfs(node.left, remaining_sum)
            dfs(node.right, remaining_sum)

            # Backtrack: remove the current node's value from the path
            current_path.pop()

        dfs(root, targetSum)
        return results