class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        current = head

        while current:
            next_node = current.next

            # Find the correct insertion point in the sorted list
            # 'prev' will point to the node *before* the insertion point
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert 'current' node into the sorted list
            current.next = prev.next
            prev.next = current

            # Move to the next node in the original unsorted list
            current = next_node

        return dummy.next