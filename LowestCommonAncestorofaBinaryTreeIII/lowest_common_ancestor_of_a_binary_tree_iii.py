# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ptr_p, ptr_q = p, q

        while ptr_p != ptr_q:
            # If ptr_p reaches the end (None), redirect it to q's starting position.
            # Otherwise, move it up to its parent.
            ptr_p = ptr_p.parent if ptr_p else q

            # If ptr_q reaches the end (None), redirect it to p's starting position.
            # Otherwise, move it up to its parent.
            ptr_q = ptr_q.parent if ptr_q else p

        return ptr_p