class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height_of_special_binary_tree(root: TreeNode) -> int:
    if root is None:
        return -1
    
    left_height = height_of_special_binary_tree(root.left)
    right_height = height_of_special_binary_tree(root.right)
    
    return 1 + max(left_height, right_height)