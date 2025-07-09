from typing import Optional

class ListNode:
    def __init__(self, val=0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        prev_group_tail = dummy_head
        current = head
        group_num = 1

        while current:
            group_head = current
            actual_group_len = 0
            temp_current = current
            group_tail = None
            
            for _ in range(group_num):
                if temp_current is None:
                    break
                actual_group_len += 1
                group_tail = temp_current
                temp_current = temp_current.next
            
            next_group_head = temp_current

            if actual_group_len % 2 == 0:
                prev = None
                curr = group_head
                count = 0
                while count < actual_group_len:
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node
                    count += 1
                
                prev_group_tail.next = prev
                group_head.next = next_group_head
                prev_group_tail = group_head
            else:
                prev_group_tail = group_tail
            
            current = next_group_head
            group_num += 1
            
        return dummy_head.next