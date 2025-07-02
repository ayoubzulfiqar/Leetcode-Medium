class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        bottom_left_value = 0

        while queue:
            level_size = len(queue)
            bottom_left_value = queue[0].val

            for _ in range(level_size):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return bottom_left_value