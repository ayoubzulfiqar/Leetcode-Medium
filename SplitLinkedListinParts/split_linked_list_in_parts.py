class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        base_size = n // k
        remainder = n % k

        result = [None] * k

        curr = head
        for i in range(k):
            part_size = base_size + (1 if i < remainder else 0)

            result[i] = curr

            if part_size > 0:
                for _ in range(part_size - 1):
                    if curr:
                        curr = curr.next
                    else:
                        break

                if curr:
                    next_part_head = curr.next
                    curr.next = None
                    curr = next_part_head
            else:
                pass

        return result