class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: TreeNode) -> list[list[int]]:
        result = []

        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            current_height = 1 + max(left_height, right_height)

            while len(result) <= current_height:
                result.append([])

            result[current_height].append(node.val)

            return current_height

        dfs(root)
        return result