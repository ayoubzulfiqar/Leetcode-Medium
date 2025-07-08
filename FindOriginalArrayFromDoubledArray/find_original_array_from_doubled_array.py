import collections

class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if len(changed) % 2 != 0:
            return []

        counts = collections.Counter(changed)
        original = []

        sorted_nums = sorted(counts.keys())

        for num in sorted_nums:
            if counts[num] == 0:
                continue

            if num == 0:
                if counts[0] % 2 != 0:
                    return []
                
                original.extend([0] * (counts[0] // 2))
                counts[0] = 0
            else:
                double_num = num * 2
                
                if counts[double_num] < counts[num]:
                    return []
                
                original.extend([num] * counts[num])
                
                counts[double_num] -= counts[num]
                
                counts[num] = 0
        
        return original