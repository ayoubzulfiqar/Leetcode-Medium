class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_all_left(root)

    def _push_all_left(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        current_node = self.stack.pop()
        if current_node.right:
            self._push_all_left(current_node.right)
        return current_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0