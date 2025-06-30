class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Phase 1: Detect cycle and find meeting point
        # Move slow by 1, fast by 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # If no cycle detected (fast reached end of list)
        if not fast or not fast.next:
            return None
        
        # Phase 2: Find the starting node of the cycle
        # Reset one pointer to head, move both by 1
        # They will meet at the cycle start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow