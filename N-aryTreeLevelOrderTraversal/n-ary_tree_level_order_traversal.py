import collections

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            current_level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(current_level_values)
        return result