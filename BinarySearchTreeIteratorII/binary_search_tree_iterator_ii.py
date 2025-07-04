class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []
        self.pointer = -1

        def inorder_traverse(node):
            if not node:
                return
            inorder_traverse(node.left)
            self.nodes.append(node.val)
            inorder_traverse(node.right)

        inorder_traverse(root)

    def next(self) -> int:
        self.pointer += 1
        return self.nodes[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer + 1 < len(self.nodes)

    def prev(self) -> int:
        self.pointer -= 1
        return self.nodes[self.pointer]

    def hasPrev(self) -> bool:
        return self.pointer - 1 >= 0