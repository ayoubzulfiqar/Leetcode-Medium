import collections

class Solution:
    def findLatestStep(self, arr: list[int], m: int) -> int:
        n = len(arr)

        group_lengths = [0] * (n + 2)
        count_of_lengths = collections.Counter()
        latest_step = -1

        for step in range(1, n + 1):
            pos = arr[step - 1]

            left_adjacent_len = group_lengths[pos - 1]
            right_adjacent_len = group_lengths[pos + 1]

            new_total_len = left_