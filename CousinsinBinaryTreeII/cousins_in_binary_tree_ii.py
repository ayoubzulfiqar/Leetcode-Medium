import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceCousinsSum(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        level_sums = collections.defaultdict(int)
        parent_children_sum_map = {}
        node_parent_map = {}

        q = collections.deque([(root, 0, None)])

        while q:
            node, depth, parent = q.popleft()

            if node is None:
                continue

            level_sums[depth] += node.val
            node_parent_map[node] = parent

            if node.left:
                q.append((node.left, depth + 1, node))
                parent_children_sum_map.setdefault(