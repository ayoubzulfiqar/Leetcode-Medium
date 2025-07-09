from typing import Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)

        def build_graph(node):
            if not node:
                return

            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
                build_graph(node.left)
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
                build_graph(node.right)

        build_graph(root)

        q = deque([(start, 0)])
        visited = {start}
        max_time = 0

        while q:
            curr_node_val, curr_time = q.popleft()
            max_time = max(max_time, curr_time)

            for neighbor in adj[curr_node_val]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, curr_time + 1))

        return max_time