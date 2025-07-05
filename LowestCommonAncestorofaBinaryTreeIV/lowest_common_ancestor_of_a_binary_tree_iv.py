class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'list[TreeNode]') -> 'TreeNode':
        self.nodes_set = set(nodes)

        def dfs(node: 'TreeNode') -> 'TreeNode':
            if node is None:
                return None

            left_lca = dfs(node.left)
            right_lca = dfs(node.right)

            is_current_node_target = (node in self.nodes_set)

            if is_current_node_target:
                return node
            else:
                if left_lca is not None and right_lca is not None:
                    return node
                elif left_lca is not None:
                    return left_lca
                elif right_lca is not None:
                    return right_lca
                else:
                    return None

        return dfs(root)