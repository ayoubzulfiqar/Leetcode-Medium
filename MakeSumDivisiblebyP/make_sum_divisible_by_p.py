class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        total_sum_mod_p = 0
        for num in nums:
            total_sum_mod_p = (total_sum_mod_p + num) % p
        if total_sum_mod_p == 0:
            return 0
        target_remainder = total_sum_mod_p
        min_len = n
        remainder_map = {0: -1}
        current_prefix_sum_mod_p = 0
        for i in range(n):
            current_prefix_sum_mod_p = (current_prefix_sum_mod_p + nums[i]) % p
            required_prev_remainder = (current_prefix_sum_mod_p - target_remainder + p) % p
            if required_prev_remainder in remainder_map:
                prev_index = remainder_map[required_prev_remainder]
                min_len = min(min_len, i - prev_index)
            remainder_map[current_prefix_sum_mod_p] = i
        if min_len == n:
            return -1
        else:
            return min_len