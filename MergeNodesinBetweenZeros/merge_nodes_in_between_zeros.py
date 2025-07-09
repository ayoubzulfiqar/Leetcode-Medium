class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current_new_node = dummy_head

        current_original_node = head.next
        current_sum = 0

        while current_original_node is not None:
            if current_original_node.val != 0:
                current_sum += current_original_node.val
            else:
                new_node = ListNode(current_sum)
                current_new_node.next = new_node
                current_new_node = new_node
                current_sum = 0
            
            current_original_node = current_original_node.next
        
        return dummy_head.next