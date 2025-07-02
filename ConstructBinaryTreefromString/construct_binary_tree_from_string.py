class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None

        def parse(current_idx):
            start_num_idx = current_idx
            if s[current_idx] == '-':
                current_idx += 1
            
            while current_idx < len(s) and s[current_idx].isdigit():
                current_idx += 1
            
            val = int(s[start_num_idx:current_idx])
            node = TreeNode(val)

            if current_idx < len(s) and s[current_idx] == '(':
                current_idx += 1
                node.left, current_idx = parse(current_idx)
                current_idx += 1 
            
            if current_idx < len(s) and s[current_idx] == '(':
                current_idx += 1
                node.right, current_idx = parse(current_idx)
                current_idx += 1

            return node, current_idx

        root, _ = parse(0)
        return root