class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def build(in_start: int, in_end: int, post_start: int, post_end: int) -> TreeNode:
            if in_start > in_end or post_start > post_end:
                return None
            
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            root_idx_inorder = inorder_map[root_val]
            
            nums_left = root_idx_inorder - in_start
            
            root.left = build(in_start, root_idx_inorder - 1, post_start, post_start + nums_left - 1)
            root.right = build(root_idx_inorder + 1, in_end, post_start + nums_left, post_end - 1)
            
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)