import collections

class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        counts = collections.Counter(nums)
        ends = collections.Counter()

        for num in nums:
            if counts[num] == 0:
                continue

            if ends[num - 1] > 0:
                ends[num - 1] -= 1
                ends[num] += 1
                counts[num] -= 1
            elif counts[num + 1] > 0 and counts[num + 2] > 0:
                counts[num] -= 1
                counts[num + 1] -= 1
                counts[num + 2] -= 1
                ends[num + 2] += 1
            else:
                return False
        
        return True