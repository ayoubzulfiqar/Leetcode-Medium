class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        diff_array = [0] * length

        for start_idx, end_idx, inc in updates:
            diff_array[start_idx] += inc
            if end_idx + 1 < length:
                diff_array[end_idx + 1] -= inc

        for i in range(1, length):
            diff_array[i] += diff_array[i - 1]

        return diff_array