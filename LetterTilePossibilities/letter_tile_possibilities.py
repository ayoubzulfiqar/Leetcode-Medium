import collections

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = collections.Counter(tiles)
        
        def dfs(current_counts):
            total_sequences = 0
            for char in current_counts:
                if current_counts[char] > 0:
                    current_counts[char] -= 1
                    total_sequences += 1
                    total_sequences += dfs(current_counts)
                    current_counts[char] += 1
            return total_sequences

        return dfs(counts)