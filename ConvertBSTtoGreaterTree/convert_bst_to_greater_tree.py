class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.current_sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        self.convertBST(root.right)

        self.current_sum += root.val
        root.val = self.current_sum

        self.convertBST(root.left)

        return root