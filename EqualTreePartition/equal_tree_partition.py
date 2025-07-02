import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        sums_count = collections.Counter()

        def dfs(node):
            if not node:
                return 0
            
            current_sum = node.val + dfs(node.left) + dfs(node.right)
            sums_count[current_sum] += 1
            return current_sum

        total_sum = dfs(root)

        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2

        if target_sum == 0:
            return sums_count[0] >= 2
        
        return sums_count[target_sum] >= 1