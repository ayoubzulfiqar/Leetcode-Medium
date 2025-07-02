import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = collections.defaultdict(list)
        val_to_node = {}

        def build_graph(node, parent):
            if not node:
                return

            val_to_node[node.val] = node

            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                build_graph(node.left, node)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                build_graph(node.right, node)

        build_graph(root, None)

        q = collections.deque([(k, 0)])
        visited = {k}

        while q:
            curr_val, dist = q.popleft()
            
            curr_node_obj = val_to_node[curr_val]

            if not curr_node_obj.left and not curr_node_obj.right:
                return curr_val

            for neighbor_val in graph[curr_val]:
                if neighbor_val not in visited:
                    visited.add(neighbor_val)
                    q.append((neighbor_val, dist + 1))
        
        return -1