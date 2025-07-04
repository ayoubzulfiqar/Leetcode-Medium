class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        sorted_nodes = []

        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            sorted_nodes.append(node.val)
            inorder_traversal(node.right)
        
        inorder_traversal(root)

        def build_balanced_bst_from_sorted_list(start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            root_node = TreeNode(sorted_nodes[mid])
            root_node.left = build_balanced_bst_from_sorted_list(start, mid - 1)
            root_node.right = build_balanced_bst_from_sorted_list(mid + 1, end)
            return root_node

        return build_balanced_bst_from_sorted_list(0, len(sorted_nodes) - 1)