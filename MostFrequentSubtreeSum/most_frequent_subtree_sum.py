import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        sum_counts = collections.Counter()

        def post_order_traverse(node):
            if not node:
                return 0

            left_sum = post_order_traverse(node.left)
            right_sum = post_order_traverse(node.right)

            current_subtree_sum = node.val + left_sum + right_sum
            sum_counts[current_subtree_sum] += 1

            return current_subtree_sum

        post_order_traverse(root)

        if not sum_counts:
            return []

        max_freq = 0
        for count in sum_counts.values():
            if count > max_freq:
                max_freq = count
        
        result = []
        for s, freq in sum_counts.items():
            if freq == max_freq:
                result.append(s)
        
        return result