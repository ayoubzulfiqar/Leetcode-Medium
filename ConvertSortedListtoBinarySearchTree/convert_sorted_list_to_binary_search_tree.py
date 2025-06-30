class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        current = head
        n = 0
        while current:
            n += 1
            current = current.next

        self.head = head

        def _convert(start: int, end: int) -> TreeNode:
            if start > end:
                return None

            mid = (start + end) // 2

            left_child = _convert(start, mid - 1)

            root = TreeNode(self.head.val)
            root.left = left_child

            self.head = self.head.next

            root.right = _convert(mid + 1, end)

            return root

        return _convert(0, n - 1)