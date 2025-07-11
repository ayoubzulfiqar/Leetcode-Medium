class Solution:
    def minSizeSubarray(self, nums: list[int], target: int) -> int:
        n = len(nums)
        total_sum_nums = sum(nums)

        def find_min_len_for_sum(arr, target_val):
            current_sum = 0
            min_len = float('inf')
            left = 0
            for right in range(len(arr)):
                current_sum += arr[right]
                while current_sum >= target_val:
                    if current_sum == target_val:
                        min_len = min(min_len, right - left + 1)
                    current_sum -= arr[left]
                    left += 1
            return min_len if min_len != float('inf') else -1

        num_full_arrays = target // total_sum_nums
        remaining_target = target % total_sum_nums

        ans = float('inf')

        if remaining_target == 0:
            ans = num_full_arrays * n
        else:
            extended_nums = nums + nums
            len_remainder_part = find_min_len_for_sum(extended_nums, remaining_target)
            if len_remainder_part != -1:
                ans = num_full_arrays * n + len_remainder_part

        return ans if ans != float('inf') else -1