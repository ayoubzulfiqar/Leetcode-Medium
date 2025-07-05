class ArrayReader:
    def __init__(self, arr):
        self._arr = arr
        self._n = len(arr)

    def get(self, index: int) -> int:
        if 0 <= index < self._n:
            return self._arr[index]
        raise IndexError("Index out of bounds")

    def length(self) -> int:
        return self._n

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        n = reader.length()

        if n == 0:
            return -1
        if n == 1:
            return 0

        candidate = -1
        candidate_idx = -1
        count = 0

        for i in range(n):
            current_val = reader.get(i)
            if count == 0:
                candidate = current_val
                candidate_idx = i
                count = 1
            elif current_val == candidate:
                count += 1
            else:
                count -= 1
        
        actual_count = 0
        for i in range(n):
            if reader.get(i) == candidate:
                actual_count += 1

        if actual_count > n / 2:
            return candidate_idx
        else:
            return -1