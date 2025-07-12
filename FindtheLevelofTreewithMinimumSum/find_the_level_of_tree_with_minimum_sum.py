import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_level_with_minimum_sum(root: TreeNode) -> int:
    if not root:
        return 0

    q = collections.deque()
    q.append(root)

    min_sum = float('inf')
    min_level = -1
    current_level = 1

    while q:
        level_sum = 0
        level_size = len(q)

        for _ in range(level_size):
            node = q.popleft()
            level_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        if level_sum < min_sum:
            min_sum = level_sum
            min_level = current_level
        
        current_level += 1
    
    return min_level