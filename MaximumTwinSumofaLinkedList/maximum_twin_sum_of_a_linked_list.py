class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        max_twin_sum = 0
        left = 0
        right = len(values) - 1

        while left < right:
            current_twin_sum = values[left] + values[right]
            max_twin_sum = max(max_twin_sum, current_twin_sum)
            left += 1
            right -= 1
            
        return max_twin_sum