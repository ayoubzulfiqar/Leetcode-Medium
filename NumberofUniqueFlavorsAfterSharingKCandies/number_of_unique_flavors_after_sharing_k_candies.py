import collections

class Solution:
    def numberOfUniqueFlavors(self, flavors: list[int], k: int) -> int:
        freq_map = collections.Counter(flavors)
        
        current_unique_flavors = len(freq_map)
        
        excess_candy_counts = []
        for count in freq_map.values():
            if count > 1:
                excess_candy_counts.append(count - 1)
        
        excess_candy_counts.sort()
        
        for excess in excess_candy_counts:
            if k >= excess:
                k -= excess
            else:
                k = 0
                break
        
        if k > 0:
            current_unique_flavors -= k
        
        return max(0, current_unique_flavors)