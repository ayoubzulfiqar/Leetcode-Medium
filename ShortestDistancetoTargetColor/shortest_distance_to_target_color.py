import collections
import bisect

class Solution:
    def shortestDistanceColor(self, colors: list[int], queries: list[list[int]]) -> list[int]:
        color_indices = collections.defaultdict(list)
        for i, color in enumerate(colors):
            color_indices[color].append(i)

        results = []
        for index, target_color in queries:
            if target_color not in color_indices:
                results.append(-1)
                continue

            indices_of_target = color_indices[target_color]
            
            # Find the insertion point for 'index' in the sorted list 'indices_of_target'.
            # 'pos' will be the index of the first element >= 'index'.
            pos = bisect.bisect_left(indices_of_target, index)

            min_dist = float('inf')

            # Case 1: Check the element at 'pos' (if it exists).
            # This is the first element in indices_of_target that is >= 'index'.
            if pos < len(indices_of_target):
                min_dist = min(min_dist, abs(indices_of_target[pos] - index))

            # Case 2: Check the element at 'pos - 1' (if it exists).
            # This is the last element in indices_of_target that is < 'index'.
            if pos > 0:
                min_dist = min(min_dist, abs(indices_of_target[pos - 1] - index))
            
            results.append(min_dist)
            
        return results