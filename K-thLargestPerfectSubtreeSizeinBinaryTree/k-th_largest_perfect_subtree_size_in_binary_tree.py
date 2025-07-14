class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestPerfectSubtreeSize(self, root: TreeNode, k: int) -> int:
        
        perfect_subtree_sizes = []

        def dfs(node):
            # Returns (is_perfect_subtree_rooted_here, height_of_perfect_subtree)
            # height_of_perfect_subtree is -1 for an empty tree (base case)
            # height_of_perfect_subtree is 0 for a single node (leaf)
            
            if node is None:
                return (True, -1) 

            left_is_perfect, left_height = dfs(node.left)
            right_is_perfect, right_height = dfs(node.right)

            if left_is_perfect and right_is_perfect and left_height == right_height:
                # This subtree is perfect
                current_height = left_height + 1
                current_size = (1 << (current_height + 1)) - 1
                perfect_subtree_sizes.append(current_size)
                return (True, current_height)
            else:
                # This subtree is not perfect rooted at 'node'
                return (False, -1) 

        dfs(root)

        perfect_subtree_sizes.sort(reverse=True)

        if k > len(perfect_subtree_sizes):
            return -1
        else:
            return perfect_subtree_sizes[k-1]