import collections

class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        val_to_indices = collections.defaultdict(list)
        for i, num in enumerate(nums):
            val_to_indices[num].append(i)

        max_len = 0

        for indices_list in val_to_indices.values():
            if not indices_list:
                continue

            left_ptr = 0
            for right_ptr in range(len(indices_list)):
                current_count_of_X = right_ptr - left_ptr + 1
                original_subarray_length = indices_list[right_ptr] - indices_list[left_ptr] + 1
                elements_to_delete = original_subarray_length - current_count_of_X

                while elements_to_delete > k:
                    left_ptr +=