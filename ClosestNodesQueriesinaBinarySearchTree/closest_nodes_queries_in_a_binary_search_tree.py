class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestNodes(self, root: TreeNode, queries: list[int]) -> list[list[int]]:
        sorted_vals = []

        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            sorted_vals.append(node.val)
            inorder_traversal(node.right)

        inorder_traversal(root)

        answer = []
        import bisect 

        for q in queries:
            mini = -1
            maxi = -1

            idx_maxi = bisect.bisect_left(sorted_vals, q)
            if idx_maxi < len(sorted_vals):
                maxi = sorted_vals[idx_maxi]

            idx_mini = bisect.bisect_right(sorted_vals, q)
            if idx_mini > 0:
                mini = sorted_vals[idx_mini - 1]
            
            answer.append([mini, maxi])
        
        return answer