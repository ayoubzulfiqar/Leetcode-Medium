import collections

class Solution:
    def findMaximumMEX(self, nums: list[int], value: int) -> int:
        remainder_counts = collections.Counter()
        for num in nums:
            remainder_counts[num % value] += 1
        
        mex = 0
        while True:
            target_remainder = mex % value
            if remainder_counts[target_remainder] > 0:
                remainder_counts[target_remainder] -= 1
                mex += 1
            else:
                break
        
        return mex