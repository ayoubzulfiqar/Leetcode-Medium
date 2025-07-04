class ImmutableListNode:
    def __init__(self, val: int, next_node: 'ImmutableListNode' = None):
        self._val = val
        self._next = next_node

    def printValue(self) -> None:
        print(self._val)

    def getNext(self) -> 'ImmutableListNode':
        return self._next

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head is None:
            return
        
        self.printLinkedListInReverse(head.getNext())
        head.printValue()

if __name__ == "__main__":
    node4 = ImmutableListNode(4)
    node3 = ImmutableListNode(3, node4)
    node2 = ImmutableListNode(2, node3)
    node1 = ImmutableListNode(1, node2)

    solution = Solution()

    solution.printLinkedListInReverse(node1)

    print() 
    solution.printLinkedListInReverse(None)

    print()
    single_node = ImmutableListNode(100)
    solution.printLinkedListInReverse(single_node)

    print()
    node6 = ImmutableListNode(6)
    node5 = ImmutableListNode(5, node6)
    solution.printLinkedListInReverse(node5)