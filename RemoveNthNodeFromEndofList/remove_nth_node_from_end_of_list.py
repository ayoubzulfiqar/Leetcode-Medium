class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        # Advance first pointer so that the gap between first and second is n nodes
        # We advance first n+1 steps to ensure second is at the node *before* the one to be removed
        for _ in range(n + 1):
            first = first.next

        # Move first to the end, maintaining the gap
        # When first reaches None, second will be at the node just before the one to be removed
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next