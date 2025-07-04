class ArrayReader:
    def __init__(self, arr):
        self._arr = arr

    def compare(self, index1: int, index2: int) -> int:
        if self._arr[index1] > self._arr[index2]:
            return 1
        elif self._arr[index1] < self._arr[index2]:
            return -1
        else:
            return 0

    def length(self) -> int:
        return len(self._arr)

def findLargestIndex(reader: 'ArrayReader') -> int:
    n = reader.length()
    if n == 0:
        return -1
    
    max_idx = 0
    
    for i in range(1, n):
        if reader.compare(i, max_idx) == 1:
            max_idx = i
            
    return max_idx