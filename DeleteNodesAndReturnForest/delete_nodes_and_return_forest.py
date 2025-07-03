class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        to_delete_set = set(to_delete)
        forest_roots = []

        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete_set:
                if node.left:
                    forest_roots.append(node.left)
                if node.right:
                    forest_roots.append(node.right)
                return None
            else:
                return node

        remaining_root = dfs(root)
        if remaining_root:
            forest_roots.append(remaining_root)

        return forest_roots