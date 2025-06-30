import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        levels = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            current_level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(current_level_values)

        return levels[::-1]