class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return True, 0

            is_left_uni, left_val = dfs(node.left)
            is_right_uni, right_val = dfs(node.right)

            current_is_univalue = True

            if node.left:
                if not is_left_uni or left_val != node.val:
                    current_is_univalue = False
            
            if node.right:
                if not is_right_uni or right_val != node.val:
                    current_is_univalue = False
            
            if current_is_univalue:
                self.count += 1
            
            return current_is_univalue, node.val

        dfs(root)
        return self.count