class Node:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

def doubly_linked_list_to_array(head: Node) -> list:
    """
    Converts a doubly linked list to a Python list (array).

    Args:
        head: The head node of the doubly linked list.

    Returns:
        A list containing the values of the nodes in the order they appear
        in the doubly linked list. Returns an empty list if the head is None.
    """
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result

if __name__ == '__main__':
    # Example 1: Empty list
    head1 = None
    arr1 = doubly_linked_list_to_array(head1)
    print(f"List: None -> Array: {arr1}") # Expected: []

    # Example 2: Single node list
    head2 = Node(10)
    arr2 = doubly_linked_list_to_array(head2)
    print(f"List: 10 -> Array: {arr2}") # Expected: [10]

    # Example 3: Multiple node list
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3

    head3 = node1
    arr3 = doubly_linked_list_to_array(head3)
    print(f"List: 1 <-> 2 <-> 3 <-> 4 -> Array: {arr3}") # Expected: [1, 2, 3, 4]

    # Example 4: Another multiple node list
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')

    node_a.next = node_b
    node_b.prev = node_a
    node_b.next = node_c
    node_c.prev = node_b

    head4 = node_a
    arr4 = doubly_linked_list_to_array(head4)
    print(f"List: A <-> B <-> C -> Array: {arr4}") # Expected: ['A', 'B', 'C']