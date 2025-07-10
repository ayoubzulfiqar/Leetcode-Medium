import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1

        level_sums = []
        queue = collections.deque([root])

        while queue:
            current_level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sums.append(current_level_sum)

        if len(level_sums) < k:
            return -1

        level_sums.sort(reverse=True)

        return level_sums[k - 1]