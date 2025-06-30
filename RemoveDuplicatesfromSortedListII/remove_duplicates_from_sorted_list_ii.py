class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # Check if current node is the start of a duplicate sequence
            if curr.next and curr.val == curr.next.val:
                # If it is, advance curr until it's the last node of the duplicate sequence
                # or until it's a unique node
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Now curr is at the last node of the duplicate sequence.
                # prev.next should skip all these duplicate nodes.
                prev.next = curr.next
                # Move curr to the next potential distinct node (after the skipped duplicates)
                curr = curr.next
            else:
                # If curr is not part of a duplicate sequence, it's a distinct node.
                # Move prev to curr and curr to curr.next
                prev = curr
                curr = curr.next
        
        return dummy.next