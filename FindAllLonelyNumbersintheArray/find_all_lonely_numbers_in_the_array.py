import collections

class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        counts = collections.Counter(nums)
        
        lonely_numbers = []
        
        for num in counts:
            if counts[num] == 1:
                if (num - 1) not in counts and (num + 1) not in counts:
                    lonely_numbers.append(num)
        
        return lonely_numbers