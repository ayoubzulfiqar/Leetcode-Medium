import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = collections.Counter(nums)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_map.items():
            buckets[freq].append(num)
            
        result = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result