import collections
import bisect

class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.val_to_indices = collections.defaultdict(list)
        for i, num in enumerate(arr):
            self.val_to_indices[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.val_to_indices:
            return 0
        
        indices = self.val_to_indices[value]
        
        start_idx = bisect.bisect_left(indices, left)
        end_idx = bisect.bisect_right(indices, right)
        
        return end_idx - start_idx