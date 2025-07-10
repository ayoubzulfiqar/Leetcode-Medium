import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        current = head
        while current and current.next:
            # Calculate GCD of current node's value and next node's value
            gcd_val = math.gcd(current.val, current.next.val)

            # Create a new node with the GCD value
            new_node = ListNode(gcd_val)

            # Insert the new node between current and current.next
            new_node.next = current.next
            current.next = new_node

            # Move current pointer two steps forward to the next original node
            # This skips the newly inserted GCD node and the original next node
            current = current.next.next
        
        return head