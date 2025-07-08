import heapq
import collections

class StockPrice:

    def __init__(self):
        self.prices_map = {}
        self.latest_timestamp = 0
        self.max_heap = []
        self.min_heap = []
        self.price_counts = collections.Counter()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.prices_map:
            old_price = self.prices_map[timestamp]
            self.price_counts[old_price] -= 1
        
        self.prices_map[timestamp] = price
        
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        
        heapq.heappush(self.max_heap, -price)
        heapq.heappush(self.min_heap, price)
        self.price_counts[price] += 1

    def current(self) -> int:
        return self.prices_map[self.latest_timestamp]

    def maximum(self) -> int:
        while self.price_counts[-self.max_heap[0]] == 0:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0]

    def minimum(self) -> int:
        while self.price_counts[self.min_heap[0]] == 0:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]