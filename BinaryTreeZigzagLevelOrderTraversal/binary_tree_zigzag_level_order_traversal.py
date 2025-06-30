import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])
        level = 0

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

            if level % 2 == 1:
                result.append(current_level_values[::-1])
            else:
                result.append(current_level_values)
            
            level += 1
            
        return result