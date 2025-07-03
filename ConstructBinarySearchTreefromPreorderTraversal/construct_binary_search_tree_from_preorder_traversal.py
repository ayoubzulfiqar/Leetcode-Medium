class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        self.idx = 0
        n = len(preorder)

        def build(lower_bound, upper_bound):
            if self.idx == n:
                return None
            
            val = preorder[self.idx]
            
            if not (lower_bound < val < upper_bound):
                return None
            
            node = TreeNode(val)
            self.idx += 1
            
            node.left = build(lower_bound, val)
            node.right = build(val, upper_bound)
            
            return node
        
        return build(float('-inf'), float('inf'))