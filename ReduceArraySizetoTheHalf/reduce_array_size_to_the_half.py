import collections

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counts = collections.Counter(arr)
        
        # Get frequencies and sort them in descending order
        sorted_frequencies = sorted(counts.values(), reverse=True)
        
        target_removed_count = len(arr) // 2
        
        current_removed_count = 0
        set_size = 0
        
        for freq in sorted_frequencies:
            current_removed_count += freq
            set_size += 1
            if current_removed_count >= target_removed_count:
                break
                
        return set_size