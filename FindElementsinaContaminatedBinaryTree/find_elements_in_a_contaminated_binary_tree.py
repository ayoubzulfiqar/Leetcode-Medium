class TreeNode:
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: TreeNode):
        self.recovered_values = set()

        def _recover_tree_dfs(node, val_to_assign):
            if not node:
                return

            self.recovered_values.add(val_to_assign)

            if node.left:
                _recover_tree_dfs(node.left, 2 * val_to_assign + 1)
            if node.right:
                _recover_tree_dfs(node.right, 2 * val_to_assign + 2)

        _recover_tree_dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.recovered_values