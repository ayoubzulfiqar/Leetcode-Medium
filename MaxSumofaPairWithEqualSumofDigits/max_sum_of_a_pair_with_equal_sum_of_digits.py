from collections import defaultdict

class Solution:
    def _get_digit_sum(self, n: int) -> int:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    def maxSum(self, nums: list[int]) -> int:
        digit_sum_map = defaultdict(lambda: [0, 0]) 

        for num in nums:
            s = self._get_digit_sum(num)
            
            if num > digit_sum_map[s][0]:
                digit_sum_map[s][1] = digit_sum_map[s][0]
                digit_sum_map[s][0] = num
            elif num > digit_sum_map[s][1]:
                digit_sum_map[s][1] = num
        
        max_total_sum = -1

        for s_key in digit_sum_map:
            if digit_sum_map[s_key][1] > 0: 
                current_pair_sum = digit_sum_map[s_key][0] + digit_sum_map[s_key][1]
                max_total_sum = max(max_total_sum, current_pair_sum)
        
        return max_total_sum