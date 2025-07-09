import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = collections.deque([(root, 0)])

        while q:
            level_size = len(q)
            
            nodes_at_this_level = []
            
            current_level = q[0][1] 

            for _ in range(level_size):
                node, _ = q.popleft()
                nodes_at_this_level.append(node)
                
                if node.left:
                    q.append((node.left, current_level + 1))
                    q.append((node.right, current_level + 1))
            
            if current_level % 2 == 1:
                values_to_reverse = [node.val for node in nodes_at_this_level]
                values_to_reverse.reverse()
                
                for i in range(len(nodes_at_this_level)):
                    nodes_at_this_level[i].val = values_to_reverse[i]
        
        return root