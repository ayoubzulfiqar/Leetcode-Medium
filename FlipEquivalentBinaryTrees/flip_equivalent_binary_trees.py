class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
            
        if root1.val != root2.val:
            return False
            
        # Case 1: No flip at current node
        # Check if root1's left matches root2's left AND root1's right matches root2's right
        option1 = self.flipEquiv(root1.left, root2.left) and \
                  self.flipEquiv(root1.right, root2.right)
                  
        # Case 2: Flip at current node
        # Check if root1's left matches root2's right AND root1's right matches root2's left
        option2 = self.flipEquiv(root1.left, root2.right) and \
                  self.flipEquiv(root1.right, root2.left)
                  
        return option1 or option2