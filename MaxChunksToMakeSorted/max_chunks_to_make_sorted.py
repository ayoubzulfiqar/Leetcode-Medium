class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        chunks = 0
        current_max = 0
        n = len(arr)

        for i in range(n):
            current_max = max(current_max, arr[i])
            if current_max == i:
                chunks += 1
        
        return chunks