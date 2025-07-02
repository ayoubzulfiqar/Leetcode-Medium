import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.val_to_indices = {}
        for i, num in enumerate(nums):
            if num not in self.val_to_indices:
                self.val_to_indices[num] = []
            self.val_to_indices[num].append(i)

    def pick(self, target: int) -> int:
        indices_list = self.val_to_indices[target]
        return random.choice(indices_list)