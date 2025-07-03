class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        postorder_map = {val: i for i, val in enumerate(postorder)}

        def build(pre_start: int, pre_end: int, post_start: int, post_end: int) -> TreeNode:
            if pre_start > pre_end:
                return None

            if pre_start == pre_end:
                return TreeNode(preorder[pre_start])

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # The next element in preorder (preorder[pre_start + 1]) is the root of the left subtree.
            # This logic assumes that if a child exists, it's the left child.
            # If the tree has only a right child, this will effectively build it as a left child,
            # which is acceptable given "If there exist multiple answers, you can return any of them."
            left_root_val = preorder[pre_start + 1]

            # Find the index of the left_root_val in the postorder traversal.
            # This index determines the boundary between left and right subtrees in postorder.
            left_root_idx_in_post = postorder_map[left_root_val]

            # Calculate the size of the left subtree.
            # It's the number of elements from post_start to left_root_idx_in_post (inclusive).
            left_subtree_size = left_root_idx_in_post - post_start + 1

            # Recursively build the left subtree
            # Preorder for left: from pre_start + 1 to pre_start + left_subtree_size
            # Postorder for left: from post_start to left_root_idx_in_post
            root.left = build(pre_start + 1, pre_start + left_subtree_size,
                              post_start, left_root_idx_in_post)

            # Recursively build the right subtree
            # Preorder for right: from pre_start + left_subtree_size + 1 to pre_end
            # Postorder for right: from left_root_idx_in_post + 1 to post_end - 1 (excluding the current root)
            root.right = build(pre_start + left_subtree_size + 1, pre_end,
                               left_root_idx_in_post + 1, post_end - 1)

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)