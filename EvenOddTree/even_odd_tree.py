import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        q = collections.deque([root])
        level = 0

        while q:
            level_size = len(q)
            prev_val = None

            for _ in range(level_size):
                node = q.popleft()

                if level % 2 == 0:  # Even-indexed level
                    if node.val % 2 == 0:  # Must be odd
                        return False
                    if prev_val is not None and node.val <= prev_val:  # Must be strictly increasing
                        return False
                else:  # Odd-indexed level
                    if node.val % 2 != 0:  # Must be even
                        return False
                    if prev_val is not None and node.val >= prev_val:  # Must be strictly decreasing
                        return False
                
                prev_val = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        
        return True