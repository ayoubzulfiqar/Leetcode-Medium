import collections

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        counts = collections.Counter()
        for row in matrix:
            if row[0] == 1:
                normalized_row = tuple(1 - x for x in row)
            else:
                normalized_row = tuple(row)
            counts[normalized_row] += 1
        
        return max(counts.values()) if counts else 0