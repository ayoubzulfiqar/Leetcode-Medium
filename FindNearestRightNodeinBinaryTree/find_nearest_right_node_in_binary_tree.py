import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findNearestRightNode(root: TreeNode, target_node: TreeNode) -> TreeNode:
    if not root or not target_node:
        return None

    queue = collections.deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        found_target_in_this_level = False

        for i in range(level_size):
            current_node = queue.popleft()

            if found_target_in_this_level:
                return current_node

            if current_node == target_node:
                found_target_in_this_level = True
                if i == level_size - 1: # Target is the last node in its level
                    return None

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    
    return None