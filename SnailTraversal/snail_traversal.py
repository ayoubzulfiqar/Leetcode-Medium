import collections

class Solution:
    def snail(self, nums: list[int], rowsCount: int, colsCount: int) -> list[list[int]]:
        if rowsCount * colsCount != len(nums):
            return []

        result = [[0] * colsCount for _ in range(rowsCount)]
        
        num_idx = 0
        for j in range(colsCount):
            if j % 2 == 0:  # Even column: traverse down
                for i in range(rowsCount):
                    result[i][j] = nums[num_idx]
                    num_idx += 1
            else:  # Odd column: traverse up
                for i in range(rowsCount - 1, -1, -1):
                    result[i][j] = nums[num_idx]
                    num_idx += 1
        
        return result