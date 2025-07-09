class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            current_sum = node.val + left_sum + right_sum
            current_count = 1 + left_count + right_count

            average = current_sum // current_count

            if node.val == average:
                self.count += 1

            return current_sum, current_count

        dfs(root)
        return self.count