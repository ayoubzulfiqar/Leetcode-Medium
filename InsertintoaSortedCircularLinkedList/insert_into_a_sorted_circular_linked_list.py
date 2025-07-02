class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def insert(head: 'Node', insertVal: int) -> 'Node':
    newNode = Node(insertVal)

    if not head:
        newNode.next = newNode
        return newNode

    curr = head
    
    while True:
        next_node = curr.next

        if curr.val <= insertVal <= next_node.val:
            break
        
        elif curr.val > next_node.val:
            if insertVal >= curr.val or insertVal <= next_node.val:
                break
        
        elif next_node == head:
            break
            
        curr = next_node
    
    newNode.next = curr.next
    curr.next = newNode
    
    return head