from typing import Optional

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_diff = 0

        def dfs(node, min_ancestor_val, max_ancestor_val):
            if not node:
                return

            self.max_diff = max(self.max_diff, abs(node.val - min_ancestor_val), abs(node.val - max_ancestor_val))

            new_min_ancestor_val = min(min_ancestor_val, node.val)
            new_max_ancestor_val = max(max_ancestor_val, node.val)

            dfs(node.left, new_min_ancestor_val, new_max_ancestor_val)
            dfs(node.right, new_min_ancestor_val, new_max_ancestor_val)

        dfs(root, root.val, root.val)

        return self.max_diff