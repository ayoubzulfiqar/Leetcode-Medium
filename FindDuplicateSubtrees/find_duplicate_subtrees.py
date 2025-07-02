import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:
        counts = collections.defaultdict(int)
        res = []

        def dfs(node):
            if not node:
                return "#"

            left_s = dfs(node.left)
            right_s = dfs(node.right)

            s = left_s + "," + str(node.val) + "," + right_s
            
            counts[s] += 1
            if counts[s] == 2:
                res.append(node)
            
            return s
        
        dfs(root)
        return res