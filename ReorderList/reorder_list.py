class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        # slow will be the end of the first half
        # fast will be at the end of the list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # head1 is the first half
        # head2 is the second half
        head1 = head
        head2 = slow.next
        slow.next = None # Break the link between the two halves

        # Step 2: Reverse the second half
        def reverseList(node):
            prev = None
            curr = node
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        head2 = reverseList(head2)

        # Step 3: Merge the two halves
        curr1 = head1
        curr2 = head2
        while curr1 and curr2:
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2