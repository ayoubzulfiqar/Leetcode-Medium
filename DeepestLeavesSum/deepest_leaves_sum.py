import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = collections.deque([root])
        current_level_sum = 0

        while queue:
            level_size = len(queue)
            current_level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return current_level_sum