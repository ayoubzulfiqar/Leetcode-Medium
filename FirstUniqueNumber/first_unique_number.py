import collections

class FirstUnique:

    def __init__(self, nums: list[int]):
        self.counts = collections.Counter()
        self.unique_queue = collections.deque()

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.unique_queue and self.counts[self.unique_queue[0]] > 1:
            self.unique_queue.popleft()
        
        if self.unique_queue:
            return self.unique_queue[0]
        else:
            return -1

    def add(self, value: int) -> None:
        self.counts[value] += 1
        
        if self.counts[value] == 1:
            self.unique_queue.append(value)