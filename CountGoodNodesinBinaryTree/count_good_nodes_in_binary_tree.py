class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, max_so_far):
            if not node:
                return

            if node.val >= max_so_far:
                self.count += 1

            new_max_so_far = max(max_so_far, node.val)

            dfs(node.left, new_max_so_far)
            dfs(node.right, new_max_so_far)

        dfs(root, float('-inf'))
        return self.count