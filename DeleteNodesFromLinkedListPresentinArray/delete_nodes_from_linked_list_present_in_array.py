class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, nums: list[int], head: ListNode) -> ListNode:
        values_to_remove = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val in values_to_remove:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next