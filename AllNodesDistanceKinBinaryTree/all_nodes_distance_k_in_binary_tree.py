import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target_val: int, k: int) -> list[int]:
        parent_map = {}
        target_node = None

        def build_parent_map_and_find_target(node, parent=None):
            nonlocal target_node
            if node:
                parent_map[node] = parent
                if node.val == target_val:
                    target_node = node
                build_parent_map_and_find_target(node.left, node)
                build_parent_map_and_find_target(node.right, node)
        
        build_parent_map_and_find_target(root)

        queue = collections.deque([(target_node, 0)])
        visited = {target_node}
        result = []

        while queue:
            current_node, dist = queue.popleft()

            if dist == k:
                result.append(current_node.val)
                continue 
            
            if dist > k:
                continue

            if current_node.left and current_node.left not in visited:
                visited.add(current_node.left)
                queue.append((current_node.left, dist + 1))
            
            if current_node.right and current_node.right not in visited:
                visited.add(current_node.right)
                queue.append((current_node.right, dist + 1))
            
            if parent_map[current_node] is not None and parent_map[current_node] not in visited:
                visited.add(parent_map[current_node])
                queue.append((parent_map[current_node], dist + 1))
        
        return result