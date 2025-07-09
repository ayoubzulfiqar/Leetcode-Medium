class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        min_distance = float('inf')
        first_critical_idx = -1
        last_critical_idx = -1
        
        prev = head
        curr = head.next
        
        current_idx = 1 
        
        while curr and curr.next:
            next_node = curr.next
            
            is_local_maxima = (curr.val > prev.val and curr.val > next_node.val)
            is_local_minima = (curr.val < prev.val and curr.val < next_node.val)
            
            if is_local_maxima or is_local_minima:
                if first_critical_idx == -1:
                    first_critical_idx = current_idx
                else:
                    min_distance = min(min_distance, current_idx - last_critical_idx)
                last_critical_idx = current_idx
            
            prev = curr
            curr = next_node
            current_idx += 1
            
        if first_critical_idx == -1 or first_critical_idx == last_critical_idx:
            return [-1, -1]
        else:
            max_distance = last_critical_idx - first_critical_idx
            return [min_distance, max_distance]