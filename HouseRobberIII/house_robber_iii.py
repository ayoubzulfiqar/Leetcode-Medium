class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return [0, 0]

            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)

            rob_current = node.val + left_not_rob + right_not_rob
            not_rob_current = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)

            return [rob_current, not_rob_current]

        result_rob, result_not_rob = dfs(root)
        return max(result_rob, result_not_rob)