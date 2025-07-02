class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        current = head
        stack = []

        while current:
            if current.child:
                # If there's a next node in the current level, save it for later
                # This is the node we'll return to after flattening the child list
                if current.next:
                    stack.append(current.next)
                
                # Connect current node to its child list
                current.next = current.child
                current.child.prev = current
                
                # Nullify the child pointer as per problem requirements
                current.child = None
            
            # If current node is the end of a flattened segment (i.e., current.next is None)
            # and there are saved nodes from higher levels (stack is not empty),
            # connect current to the next node from the stack.
            # This handles returning from a child list back to the main list.
            elif not current.next and stack:
                next_level_node = stack.pop()
                current.next = next_level_node
                next_level_node.prev = current
            
            # Move to the next node in the flattened list
            current = current.next
        
        return head