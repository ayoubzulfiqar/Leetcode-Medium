import random

class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        
        self.val_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        
        idx_to_remove = self.val_to_idx[val]
        last_val = self.nums[-1]
        
        if val != last_val:
            self.nums[idx_to_remove] = last_val
            self.val_to_idx[last_val] = idx_to_remove
        
        del self.val_to_idx[val]
        self.nums.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)