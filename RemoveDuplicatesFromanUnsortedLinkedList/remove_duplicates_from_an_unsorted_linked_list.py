class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        seen = set()
        current = head
        previous = None

        while current:
            if current.val in seen:
                # This is a duplicate, remove it by skipping current
                # The previous node's next pointer should bypass the current node
                previous.next = current.next
            else:
                # Not a duplicate, add to seen and advance previous pointer
                seen.add(current.val)
                previous = current
            
            # Move to the next node in the original list structure
            current = current.next
        
        return head