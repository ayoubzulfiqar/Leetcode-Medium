class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortLinkedList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # The problem statement implies that if we take the absolute value of each node,
        # the sequence of absolute values is sorted in non-decreasing order.
        # For example, if the input is 1 -> -2 -> 3 -> -4 -> 5,
        # the absolute values are 1, 2, 3, 4, 5, which are sorted.
        # The goal is to sort the actual values, resulting in -4 -> -2 -> 1 -> 3 -> 5.
        #
        # Given the property that abs(val) sequence is sorted, it means:
        # 1. All non-negative numbers are already in ascending order relative to each other.
        # 2. All negative numbers, say N1, N2, N3 appearing in that order, satisfy
        #    abs(N1) <= abs(N2) <= abs(N3). This implies -N1 <= -N2 <= -N3,
        #    which means N1 >= N2 >= N3. So, negative numbers are in descending order
        #    of their actual values if they appear in the original list.
        #
        # The strategy is to iterate through the list.
        # Positive (or zero) numbers are in their correct relative positions.
        # Negative numbers need to be moved to the front of the list.
        # Since we are inserting them at the very beginning (new_head), and
        # they are encountered in descending order of their actual values (e.g., -1 then -2 then -3),
        # inserting them at the head will naturally place them in the correct ascending order
        # among themselves (e.g., -3 will be inserted before -2, which was inserted before -1).

        new_head = head  # This will be the head of the sorted list
        prev = head      # Pointer to the node before current
        curr = head.next # Pointer to the current node being examined

        while curr:
            if curr.val < 0:
                # Remove curr from its current position
                prev.next = curr.next

                # Insert curr at the beginning of the list
                curr.next = new_head
                new_head = curr

                # Move curr to the node that was originally after it
                # prev remains the same because the node it pointed to (curr) was removed
                curr = prev.next
            else:
                # If current node is non-negative, it's in its correct relative position.
                # Just move pointers forward.
                prev = curr
                curr = curr.next
        
        return new_head