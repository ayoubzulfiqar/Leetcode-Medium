class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []

        curr = l1
        while curr:
            stack1.append(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            stack2.append(curr.val)
            curr = curr.next

        head = None
        carry = 0

        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            current_sum = val1 + val2 + carry
            
            digit = current_sum % 10
            carry = current_sum // 10

            new_node = ListNode(digit)
            new_node.next = head
            head = new_node
            
        return head