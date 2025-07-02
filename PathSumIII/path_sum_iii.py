import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.count = 0
        self.prefix_sums = collections.defaultdict(int)
        self.prefix_sums[0] = 1

        def dfs(node, current_sum):
            if not node:
                return

            current_sum += node.val

            self.count += self.prefix_sums[current_sum - targetSum]

            self.prefix_sums[current_sum] += 1

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            self.prefix_sums[current_sum] -= 1

        dfs(root, 0)
        return self.count