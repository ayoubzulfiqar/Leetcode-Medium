class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        s1 = set()

        def collect_elements(node):
            if not node:
                return
            collect_elements(node.left)
            s1.add(node.val)
            collect_elements(node.right)

        collect_elements(root1)

        def find_match(node):
            if not node:
                return False

            complement = target - node.val
            if complement in s1:
                return True

            return find_match(node.left) or find_match(node.right)

        return find_match(root2)