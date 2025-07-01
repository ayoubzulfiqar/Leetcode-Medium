import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        # column_map stores node values grouped by their horizontal distance (column index)
        # The key is the horizontal distance, and the value is a list of node values
        column_map = collections.defaultdict(list)

        # queue for BFS, storing tuples of (node, horizontal_distance)
        queue = collections.deque([(root, 0)])

        min_hd = 0
        max_hd = 0

        while queue:
            node, hd = queue.popleft()

            # Add the current node's value to its corresponding column list
            column_map[hd].append(node.val)

            # Update min/max horizontal distances encountered
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)

            # Add left child to queue with horizontal distance hd - 1
            if node.left:
                queue.append((node.left, hd - 1))

            # Add right child to queue with horizontal distance hd + 1
            if node.right:
                queue.append((node.right, hd + 1))

        # Construct the final result list by iterating from min_hd to max_hd
        result = []
        for hd in range(min_hd, max_hd + 1):
            if hd in column_map:
                result.append(column_map[hd])
        
        return result