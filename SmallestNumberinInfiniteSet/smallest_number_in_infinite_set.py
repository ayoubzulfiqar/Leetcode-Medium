import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current_smallest = 1
        self.added_back_nums = []  # Min-heap to store numbers added back
        self.in_added_back_set = set() # Set for O(1) lookup of numbers in added_back_nums

    def popSmallest(self) -> int:
        if self.added_back_nums:
            smallest = heapq.heappop(self.added_back_nums)
            self.in_added_back_set.remove(smallest)
            return smallest
        else:
            smallest = self.current_smallest
            self.current_smallest += 1
            return smallest

    def addBack(self, num: int) -> None:
        if num < self.current_smallest and num not in self.in_added_back_set:
            heapq.heappush(self.added_back_nums, num)
            self.in_added_back_set.add(num)