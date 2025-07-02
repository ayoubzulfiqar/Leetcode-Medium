import collections

class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        freq_map = collections.Counter(nums)
        count = 0

        if k == 0:
            for num in freq_map:
                if freq_map[num] >= 2:
                    count += 1
        else:
            for num in freq_map:
                if (num + k) in freq_map:
                    count += 1
        
        return count