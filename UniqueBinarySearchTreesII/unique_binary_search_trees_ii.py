class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        if n == 0:
            return []

        def _generate(start, end):
            if start > end:
                return [None]
            
            if start == end:
                return [TreeNode(start)]

            all_trees = []
            for i in range(start, end + 1):
                left_subtrees = _generate(start, i - 1)
                right_subtrees = _generate(i + 1, end)
                
                for l_tree in left_subtrees:
                    for r_tree in right_subtrees:
                        current_root = TreeNode(i)
                        current_root.left = l_tree
                        current_root.right = r_tree
                        all_trees.append(current_root)
            return all_trees

        return _generate(1, n)