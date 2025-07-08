class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class MostRecentlyUsedQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if self.size >= self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)

    def dequeue(self) -> tuple:
        if self.size == 0:
            return None

        lru_node = self.tail.prev
        self._remove_node(lru_node)
        del self.cache[lru_node.key]
        return (lru_node.key, lru_node.value)

    def peek(self) -> tuple:
        if self.size == 0:
            return None
        mru_node = self.head.next
        return (mru_node.key, mru_node.value)

    def peek_lru(self) -> tuple:
        if self.size == 0:
            return None
        lru_node = self.tail.prev
        return (lru_node.key, lru_node.value)