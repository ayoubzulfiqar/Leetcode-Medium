class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        SENTINEL = 2147483647 

        low = 0
        high = 1

        while reader.get(high) < target:
            low = high
            high *= 2
        
        while low <= high:
            mid = low + (high - low) // 2
            val = reader.get(mid)

            if val == target:
                return mid
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1