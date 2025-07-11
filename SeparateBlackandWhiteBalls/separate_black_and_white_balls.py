class Solution:
    def minMoves(self, s: str) -> int:
        total_swaps = 0
        num_ones_seen = 0
        for char in s:
            if char == '1':
                num_ones_seen += 1
            else:
                total_swaps += num_ones_seen
        return total_swaps