class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        deletion_happened = True 

        while deletion_happened:
            deletion_happened = False
            
            current_sum = 0
            sum_map = {0: dummy} 
            
            current = dummy.next
            while current:
                current_sum += current.val
                
                if current_sum in sum_map:
                    node_before_sequence = sum_map[current_sum]
                    node_before_sequence.next = current.next
                    
                    deletion_happened = True
                    break 
                else:
                    sum_map[current_sum] = current
                
                current = current.next
                
        return dummy.next