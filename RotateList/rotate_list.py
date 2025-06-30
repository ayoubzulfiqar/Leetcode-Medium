class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        # 1. Find the length of the list and the original tail
        n = 1
        current = head
        while current.next:
            current = current.next
            n += 1
        
        # current is now the original tail
        original_tail = current 

        # 2. Calculate effective k
        # k can be larger than n, so we take k modulo n
        k_effective = k % n

        # If k_effective is 0, no rotation is needed (list returns to original state)
        if k_effective == 0:
            return head

        # 3. Connect the original tail to the original head to form a circle
        original_tail.next = head

        # 4. Find the new tail and new head
        # The new tail will be the node at position (n - k_effective - 1) from the original head (0-indexed)
        # The new head will be the node after the new tail
        steps_to_new_tail = n - k_effective - 1
        
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # new_tail is now the node that will be the last node of the rotated list

        # 5. Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head