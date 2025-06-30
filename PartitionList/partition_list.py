import collections
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes to serve as the heads of the two partitions
        # One for nodes with values less than x
        less_head = ListNode(0)
        # One for nodes with values greater than or equal to x
        greater_equal_head = ListNode(0)

        # Pointers to the current tail of each partition
        less_ptr = less_head
        greater_equal_ptr = greater_equal_head

        current = head
        while current:
            if current.val < x:
                less_ptr.next = current
                less_ptr = less_ptr.next
            else:
                greater_equal_ptr.next = current
                greater_equal_ptr = greater_equal_ptr.next
            current = current.next
        
        # Connect the tail of the 'less' partition to the head of the 'greater_equal' partition
        less_ptr.next = greater_equal_head.next
        
        # Important: Terminate the 'greater_equal' partition to avoid cycles
        # or including original list's remaining nodes if they weren't processed.
        greater_equal_ptr.next = None
        
        # The head of the partitioned list is after the dummy node of the 'less' partition
        return less_head.next