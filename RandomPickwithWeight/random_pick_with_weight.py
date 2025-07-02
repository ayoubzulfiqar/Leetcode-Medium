import random
import bisect

class Solution:

    def __init__(self, w: list[int]):
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        target = random.uniform(0, self.total_sum)
        return bisect.bisect_left(self.prefix_sums, target)