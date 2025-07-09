import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        sys.setrecursionlimit(2 * 10**5)

        def findPath(node, target_val, current_path):
            if not node:
                return False

            if node.val == target_val:
                return True

            if node.left and findPath(node.left, target_val, current_path):
                current_path.append('L')
                return True

            if node.right and findPath(node.right, target_val, current_path):
                current_path.append('R')
                return True

            return False

        path_to_start_from_root = []
        findPath(root, startValue, path_to_start_from_root)
        path_to_start_from_root.reverse() # Path from root to startValue

        path_to_dest_from_root = []
        findPath(root, destValue, path_to_dest_from_root)
        path_to_dest_from_root.reverse() # Path from root to destValue

        common_path_len = 0
        while common_path_len < len(path_to_start_from_root) and \
              common_path_len < len(path_to_dest_from_root) and \
              path_to_start_from_root[common_path_len] == path_to_dest_from_root[common_path_len]:
            common_path_len += 1

        # Directions from startValue to LCA are 'U' for each step in path_to_start_from_root after common prefix
        ups_needed = len(path_to_start_from_root) - common_path_len
        directions_up = 'U' * ups_needed

        # Directions from LCA to destValue are the remaining steps in path_to_dest_from_root
        directions_down = "".join(path_to_dest_from_root[common_path_len:])

        return directions_up + directions_down