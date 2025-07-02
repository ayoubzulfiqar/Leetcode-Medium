import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        current = self.head
        count = 0
        result = 0

        while current:
            count += 1
            if random.randrange(count) == 0:
                result = current.val
            current = current.next
        
        return result