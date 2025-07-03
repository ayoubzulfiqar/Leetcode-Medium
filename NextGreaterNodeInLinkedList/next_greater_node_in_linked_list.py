class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> list[int]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        n = len(values)
        answer = [0] * n
        stack = [] # Stores (index, value)

        for i in range(n):
            current_val = values[i]

            while stack and current_val > stack[-1][1]:
                prev_index, _ = stack.pop()
                answer[prev_index] = current_val
            
            stack.append((i, current_val))
        
        return answer