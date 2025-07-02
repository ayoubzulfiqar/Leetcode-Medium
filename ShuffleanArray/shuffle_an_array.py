import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.original_nums = list(nums)

    def reset(self) -> List[int]:
        return self.original_nums

    def shuffle(self) -> List[int]:
        shuffled_copy = list(self.original_nums)
        n = len(shuffled_copy)

        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            shuffled_copy[i], shuffled_copy[j] = shuffled_copy[j], shuffled_copy[i]
            
        return shuffled_copy