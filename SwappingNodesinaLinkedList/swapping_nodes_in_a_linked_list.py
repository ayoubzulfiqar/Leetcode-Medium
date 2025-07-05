class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        curr = head
        length = 0
        kth_node_from_beginning = None
        count = 1

        while curr:
            if count == k:
                kth_node_from_beginning = curr
            curr = curr.next
            length += 1
            count += 1
        
        target_pos_for_kth_from_end = length - k + 1
        
        curr = head
        kth_node_from_end = None
        count = 1

        while curr:
            if count == target_pos_for_kth_from_end:
                kth_node_from_end = curr
                break
            curr = curr.next
            count += 1
            
        kth_node_from_beginning.val, kth_node_from_end.val = kth_node_from_end.val, kth_node_from_beginning.val
            
        return head