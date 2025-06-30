class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        
        # Find the node just before the 'left' position
        # This will be 'prev_left_node'
        prev_left_node = dummy
        for _ in range(left - 1):
            prev_left_node = prev_left_node.next
        
        # 'start_node' is the actual 'left'-th node
        start_node = prev_left_node.next
        
        # Reverse the sublist from 'left' to 'right'
        # 'prev' will become the new head of the reversed sublist (which is the original 'right'-th node)
        # 'current' will traverse the sublist
        
        prev = None
        current = start_node
        
        # Iterate 'right - left + 1' times to reverse the segment
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        # At the end of this loop:
        # 'prev' is the new head of the reversed segment (original 'right'-th node)
        # 'start_node' is the original 'left'-th node, now its .next points to what was before it in the reversed segment
        # 'current' is the node immediately after the 'right'-th node (this is 'next_to_end_node')
        
        # Connect the parts
        # The node before the reversed segment ('prev_left_node') should point to the new head of the reversed segment ('prev')
        prev_left_node.next = prev
        
        # The original 'left'-th node ('start_node') should now point to the node immediately after the reversed segment ('current')
        start_node.next = current
        
        return dummy.next