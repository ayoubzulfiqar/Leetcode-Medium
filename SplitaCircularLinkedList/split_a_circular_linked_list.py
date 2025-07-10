class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def split_circular_list(head):
    if not head:
        return None, None

    # Handle single node list
    if head.next == head:
        return head, None

    slow = head
    fast = head

    # Find the middle (slow) and the original tail (fast or fast.next)
    # slow will be the last node of the first half
    # fast will be at the last or second to last node of the original list
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # Determine the actual tail of the original list
    # If fast.next.next == head, it means there's an odd number of nodes, and fast.next is the tail.
    # If fast.next == head, it means there's an even number of nodes, and fast is the tail.
    original_tail = fast.next if fast.next.next == head else fast

    # head1 starts at the original head
    head1 = head
    # head2 starts after slow
    head2 = slow.next

    # Make the first list circular
    slow.next = head1

    # Make the second list circular
    original_tail.next = head2

    return head1, head2