class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.smallest_string = "~"

        def dfs(node, current_path_chars):
            if not node:
                return

            char = chr(node.val + ord('a'))
            current_path_chars.append(char)

            if not node.left and not node.right:
                leaf_to_root_str = "".join(current_path_chars[::-1])
                
                if leaf_to_root_str < self.smallest_string:
                    self.smallest_string = leaf_to_root_str
                
                current_path_chars.pop()
                return

            dfs(node.left, current_path_chars)
            dfs(node.right, current_path_chars)

            current_path_chars.pop()

        dfs(root, [])

        return self.smallest_string