class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(preorder_start: int, preorder_end: int, inorder_start: int, inorder_end: int) -> TreeNode:
            if preorder_start > preorder_end or inorder_start > inorder_end:
                return None

            root_val = preorder[preorder_start]
            root = TreeNode(root_val)

            root_in_inorder_idx = inorder_map[root_val]

            nums_left_subtree = root_in_inorder_idx - inorder_start

            root.left = build(preorder_start + 1, preorder_start + nums_left_subtree,
                              inorder_start, root_in_inorder_idx - 1)

            root.right = build(preorder_start + nums_left_subtree + 1, preorder_end,
                               root_in_inorder_idx + 1, inorder_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)