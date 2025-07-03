import collections
import threading

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = collections.deque()
        self.condition = threading.Condition()

    def enqueue(self, element: int) -> None:
        with self.condition:
            while len(self.queue) == self.capacity:
                self.condition.wait()
            self.queue.append(element)
            self.condition.notify_all()

    def dequeue(self) -> int:
        with self.condition:
            while len(self.queue) == 0:
                self.condition.wait()
            element = self.queue.popleft()
            self.condition.notify_all()
            return element

    def size(self) -> int:
        with self.condition:
            return len(self.queue)