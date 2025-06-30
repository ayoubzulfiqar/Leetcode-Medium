import collections
from typing import List

class ZigzagIterator:

    def __init__(self, v: List[List[int]]):
        self.data = v
        self.queue = collections.deque()

        for i in range(len(self.data)):
            if self.data[i]:
                self.queue.append((i, 0))

    def next(self) -> int:
        list_idx, element_idx = self.queue.popleft()
        value = self.data[list_idx][element_idx]

        if element_idx + 1 < len(self.data[list_idx]):
            self.queue.append((list_idx, element_idx + 1))

        return value

    def hasNext(self) -> bool:
        return bool(self.queue)