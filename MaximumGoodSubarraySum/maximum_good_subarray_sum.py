import math

class Solution:
    def maximumGoodSubarraySum(self, nums: list[int], k: int) -> int:
        max_good_sum = -math.inf
        found_good_subarray = False

        min_prefix_for_val = {}
        current_prefix_sum_val = 0 

        for j in range(len(nums)):
            current_val = nums[j]

            target_val_1 = current_val - k
            if target_val_1 in min_prefix_for_val:
                min_ps_1 = min_prefix_for_val[target_val_1]
                candidate_sum = (current_prefix_sum_val + current_val) - min_ps_1
                max_good_sum = max(max_good_sum, candidate_sum)
                found_good_subarray = True

            target_val_2 = current_val + k
            if target_val_2 in min_prefix_for_val:
                min_ps_2 = min_prefix_for_val[target_val_2]
                candidate_sum = (current_prefix_sum_val + current_val) - min_ps_2
                max_good_sum = max(max_good_sum, candidate_sum)
                found_good