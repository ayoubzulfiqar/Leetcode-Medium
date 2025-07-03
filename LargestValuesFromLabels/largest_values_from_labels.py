import collections

class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)

        current_sum = 0
        items_selected = 0
        label_counts = collections.defaultdict(int)

        for value, label in items:
            if items_selected == numWanted:
                break

            if label_counts[label] < useLimit:
                current_sum += value
                items_selected += 1
                label_counts[label] += 1
        
        return current_sum