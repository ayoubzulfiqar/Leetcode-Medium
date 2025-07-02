class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def splitBST(root: TreeNode, target: int) -> list[TreeNode]:
    if not root:
        return [None, None]

    if root.val <= target:
        left_part_of_right_subtree, right_part_of_right_subtree = splitBST(root.right, target)
        root.right = left_part_of_right_subtree
        return [root, right_part_of_right_subtree]
    else:
        left_part_of_left_subtree, right_part_of_left_subtree = splitBST(root.left, target)
        root.left = right_part_of_left_subtree
        return [left_part_of_left_subtree, root]