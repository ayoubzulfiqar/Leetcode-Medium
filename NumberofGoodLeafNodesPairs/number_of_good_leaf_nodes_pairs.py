class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.good_pairs_count = 0

        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left_leaf_distances = dfs(node.left)
            right_leaf_distances = dfs(node.right)

            for ld in left_leaf_distances:
                for rd in right_leaf_distances:
                    if ld + rd <= distance:
                        self.good_pairs_count += 1

            current_node_leaf_distances = []
            for d in left_leaf_distances:
                if d + 1 <= distance:
                    current_node_leaf_distances.append(d + 1)
            for d in right_leaf_distances:
                if d + 1 <= distance:
                    current_node_leaf_distances.append(d + 1)

            return current_node_leaf_distances

        dfs(root)
        return self.good_pairs_count