from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            current = node
            while current:
                next_temp = current.next
                current.next = prev
                prev = current
                current = next_temp
            return prev

        reversed_head = reverseList(head)

        current = reversed_head
        carry = 0
        
        new_result_head = None 
        
        while current:
            doubled_val = current.val * 2 + carry
            
            digit = doubled_val % 10
            carry = doubled_val // 10
            
            new_node = ListNode(digit)
            
            new_node.next = new_result_head
            new_result_head = new_node
            
            current = current.next
        
        if carry > 0:
            new_node = ListNode(carry)
            new_node.next = new_result_head
            new_result_head = new_node
            
        return new_result_head