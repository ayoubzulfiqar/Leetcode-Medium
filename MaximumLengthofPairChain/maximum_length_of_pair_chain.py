class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        max_length = 0
        current_end = float('-inf')

        for left, right in pairs:
            if left > current_end:
                max_length += 1
                current_end = right
        
        return max_length