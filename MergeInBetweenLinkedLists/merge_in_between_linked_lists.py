class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    node_before_a = list1
    for _ in range(a - 1):
        node_before_a = node_before_a.next

    node_b = list1
    for _ in range(b):
        node_b = node_b.next
    node_after_b = node_b.next

    node_before_a.next = list2

    list2_tail = list2
    while list2_tail.next:
        list2_tail = list2_tail.next

    list2_tail.next = node_after_b

    return list1