from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        reversed_head = self.reverseList(head)

        current_max = 0

        dummy = ListNode()
        current_new_list_tail = dummy

        curr = reversed_head
        while curr:
            if curr.val >= current_max:
                current_max = curr.val
                current_new_list_tail.next = curr
                current_new_list_tail = curr
            curr = curr.next

        current_new_list_tail.next = None

        return self.reverseList(dummy.next)