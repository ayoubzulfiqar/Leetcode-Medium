class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        # Initialize max_avg to negative infinity to ensure any valid average is greater
        self.max_avg = float('-inf')

        # Helper function performs DFS and returns (sum, count) for the subtree rooted at 'node'
        def dfs(node):
            if not node:
                # For an empty subtree, sum is 0 and count is 0
                return 0, 0

            # Recursively get sum and count for left and right subtrees
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            # Calculate sum and count for the current subtree (including the current node)
            current_sum = node.val + left_sum + right_sum
            current_count = 1 + left_count + right_count

            # Calculate the average for the current subtree
            # current_count will always be at least 1 since 'node' is not None
            current_avg = current_sum / current_count
            
            # Update the global maximum average found so far
            self.max_avg = max(self.max_avg, current_avg)

            # Return the sum and count of the current subtree to its parent
            return current_sum, current_count

        # If the tree is empty, there are no subtrees. Return 0.0 as a default.
        # (Alternatively, float('-inf') could be used depending on exact problem spec for empty tree)
        if not root:
            return 0.0

        # Start the DFS traversal from the root
        dfs(root)

        # Return the maximum average found across all subtrees
        return self.max_avg