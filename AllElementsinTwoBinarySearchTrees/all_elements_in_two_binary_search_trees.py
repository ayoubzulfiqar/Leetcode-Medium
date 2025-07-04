class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        def inorder_traversal(node, arr):
            if not node:
                return
            inorder_traversal(node.left, arr)
            arr.append(node.val)
            inorder_traversal(node.right, arr)

        list1 = []
        inorder_traversal(root1, list1)

        list2 = []
        inorder_traversal(root2, list2)

        result = []
        p1, p2 = 0, 0
        n1, n2 = len(list1), len(list2)

        while p1 < n1 and p2 < n2:
            if list1[p1] <= list2[p2]:
                result.append(list1[p1])
                p1 += 1
            else:
                result.append(list2[p2])
                p2 += 1

        while p1 < n1:
            result.append(list1[p1])
            p1 += 1

        while p2 < n2:
            result.append(list2[p2])
            p2 += 1

        return result