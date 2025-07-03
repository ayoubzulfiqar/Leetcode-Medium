class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.current_sum = 0

        def dfs(node):
            if not node:
                return

            # Traverse the right subtree first (nodes with greater values)
            dfs(node.right)

            # Visit the current node:
            # 1. Add the current node's original value to the running sum.
            #    At this point, self.current_sum holds the sum of all original values
            #    of nodes that are strictly greater than the current node.
            #    By adding node.val, self.current_sum now holds the sum of all original values
            #    of nodes that are greater than or equal to the current node.
            self.current_sum += node.val

            # 2. Update the current node's value to this accumulated sum.
            node.val = self.current_sum

            # Traverse the left subtree (nodes with smaller values)
            dfs(node.left)

        dfs(root)
        return root