import collections

class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        edge_counts = collections.defaultdict(int)
        
        for row in wall:
            current_width = 0
            for brick_width in row[:-1]: 
                current_width += brick_width
                edge_counts[current_width] += 1
        
        max_aligned_edges = 0
        if edge_counts:
            max_aligned_edges = max(edge_counts.values())
        
        return len(wall) - max_aligned_edges