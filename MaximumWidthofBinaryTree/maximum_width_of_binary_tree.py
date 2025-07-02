import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxWidth = 0
        queue = collections.deque([(root, 0)])

        while queue:
            level_size = len(queue)
            
            first_node_original_index = queue[0][1]
            
            last_node_normalized_index = 0

            for _ in range(level_size):
                node, original_index = queue.popleft()
                
                normalized_index = original_index - first_node_original_index
                
                last_node_normalized_index = normalized_index

                if node.left:
                    queue.append((node.left, 2 * normalized_index))
                if node.right:
                    queue.append((node.right, 2 * normalized_index + 1))
            
            current_width = last_node_normalized_index + 1
            maxWidth = max(maxWidth, current_width)
        
        return maxWidth