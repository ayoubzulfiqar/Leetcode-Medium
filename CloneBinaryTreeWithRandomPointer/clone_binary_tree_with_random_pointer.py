class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        old_to_new = {}

        def dfs(node):
            if not node:
                return None

            if node in old_to_new:
                return old_to_new[node]

            new_node = Node(node.val)
            old_to_new[node] = new_node

            new_node.left = dfs(node.left)
            new_node.right = dfs(node.right)
            new_node.random = dfs(node.random)

            return new_node

        return dfs(root)