import collections

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        counts = collections.Counter(arr)
        sorted_frequencies = sorted(counts.values())
        
        unique_count = len(sorted_frequencies)
        
        for freq in sorted_frequencies:
            if k >= freq:
                k -= freq
                unique_count -= 1
            else:
                break
        
        return unique_count