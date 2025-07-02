class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        not_nine_ptr = dummy
        current = head

        # Find the rightmost digit that is not 9
        # This 'not_nine_ptr' will point to the digit that needs to be incremented.
        # If all digits are 9s, this will remain pointing to the dummy node.
        while current:
            if current.val != 9:
                not_nine_ptr = current
            current = current.next

        # Increment the value of the 'not_nine_ptr' node
        not_nine_ptr.val += 1

        # Set all digits after 'not_nine_ptr' to 0
        # These are the 9s that "rolled over" (e.g., 129 -> 130, 99 -> 100)
        current = not_nine_ptr.next
        while current:
            current.val = 0
            current = current.next

        # If the dummy node was incremented (meaning the original number was all 9s,
        # like 999 became 1000), then the dummy node is the new head.
        if dummy.val == 1:
            return dummy
        else:
            # Otherwise, the original head (or its modified version) is still the head.
            return dummy.next