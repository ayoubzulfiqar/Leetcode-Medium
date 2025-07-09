import collections

class Solution:
    def getDistances(self, arr: list[int]) -> list[int]:
        n = len(arr)
        intervals = [0] * n
        
        val_to_indices = collections.defaultdict(list)
        for i, num in enumerate(arr):
            val_to_indices[num].append(i)
            
        for val in val_to_indices:
            indices = val_to_indices[val]
            k = len(indices)
            
            if k <= 1:
                continue
            
            prefix_sums = [0] * (k + 1)
            for j in range(k):
                prefix_sums[j+1] = prefix_sums[j] + indices[j]
            
            for j in range(k):
                current_index = indices[j]
                
                # Sum of differences from elements to the left:
                # (current_index - indices[0]) + ... + (current_index - indices[j-1])
                # = j * current_index - (indices[0] + ... + indices[j-1])
                # = j * current_index - prefix_sums[j]
                left_sum_diff = j * current_index - prefix_sums[j]
                
                # Sum of differences from elements to the right:
                # (indices[j+1] - current_index) + ... + (indices[k-1] - current_index)
                # = (indices[j+1] + ... + indices[k-1]) - (k - 1 - j) * current_index
                # The sum of indices to the right is total sum of all indices - sum of indices up to current_index
                # = prefix_sums[k] - prefix_sums[j+1]
                right_sum_diff = (prefix_sums[k] - prefix_sums[j+1]) - (k - 1 - j) * current_index
                
                intervals[current_index] = left_sum_diff + right_sum_diff
                
        return intervals