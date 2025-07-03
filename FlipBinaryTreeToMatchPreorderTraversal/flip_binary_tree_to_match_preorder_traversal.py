class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: list[int]) -> list[int]:
        self.idx = 0
        self.flipped_nodes = []
        self.possible = True

        def dfs(node):
            if not node or not self.possible:
                return

            if node.val != voyage[self.idx]:
                self.possible = False
                return

            self.idx += 1

            # Check if the left child matches the next expected value in voyage
            if node.left and self.idx < len(voyage) and node.left.val == voyage[self.idx]:
                dfs(node.left)
                if not self.possible:
                    return
                dfs(node.right)
            # If left child does not match (or doesn't exist), check if the right child matches.
            # This indicates a required flip.
            elif node.right and self.idx < len(voyage) and node.right.val == voyage[self.idx]:
                self.flipped_nodes.append(node.val)
                dfs(node.right) # Traverse right child (as if it's the new left)
                if not self.possible:
                    return
                dfs(node.left)  # Traverse left child (as if it's the new right)
            # If neither child matches the next expected value, and there are children
            # that should have been matched according to voyage (or voyage expects more
            # values than available children), then it's an impossible match.
            # This case is implicitly handled by `self.idx` not reaching `len(voyage)`
            # at the end if a mismatch occurs here. No explicit `self.possible = False` is needed.

        dfs(root)

        if not self.possible or self.idx != len(voyage):
            return [-1]
        return self.flipped_nodes