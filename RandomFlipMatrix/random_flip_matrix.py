import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total_cells = m * n
        self.available_count = m * n
        self.mapping = {} 

    def flip(self) -> list[int]:
        rand_conceptual_idx = random.randrange(self.available_count)

        actual_picked_cell_idx = self.mapping.get(rand_conceptual_idx, rand_conceptual_idx)

        last_conceptual_idx = self.available_count - 1
        actual_last_cell_idx = self.mapping.get(last_conceptual_idx, last_conceptual_idx)

        self.mapping[rand_conceptual_idx] = actual_last_cell_idx
        
        self.available_count -= 1

        if last_conceptual_idx in self.mapping:
             del self.mapping[last_conceptual_idx]

        r = actual_picked_cell_idx // self.n
        c = actual_picked_cell_idx % self.n
        
        return [r, c]

    def reset(self) -> None:
        self.available_count = self.total_cells
        self.mapping.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()