class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        def _build(arr, start, end):
            if start > end:
                return None

            max_val = -1
            max_idx = -1
            for i in range(start, end + 1):
                if arr[i] > max_val:
                    max_val = arr[i]
                    max_idx = i
            
            root = TreeNode(max_val)
            
            root.left = _build(arr, start, max_idx - 1)
            root.right = _build(arr, max_idx + 1, end)
            
            return root

        return _build(nums, 0, len(nums) - 1)