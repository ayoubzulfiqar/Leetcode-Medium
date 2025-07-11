class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        count_ones = 0
        sum_non_ones = 0

        for x in nums:
            if x == 1:
                count_ones += 1
            else:
                sum_non_ones += x
        
        if sum_non_ones == 0:
            if count_ones == 0:
                return 0
            else:
                return 1
        else:
            return sum_non_ones