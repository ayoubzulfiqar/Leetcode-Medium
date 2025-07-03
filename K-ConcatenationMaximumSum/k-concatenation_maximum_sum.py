class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadane(current_arr):
            current_max = 0
            max_so_far = 0
            for x in current_arr:
                current_max += x
                max_so_far = max(max_so_far, current_max)
                if current_max < 0:
                    current_max = 0
            return max_so_far

        if k == 1:
            return kadane(arr) % MOD

        max_single_arr_sum = kadane(arr)
        total_sum = sum(arr)

        max_prefix_sum = 0
        current_sum = 0
        for x in arr:
            current_sum += x
            max_prefix_sum = max(max_prefix_sum, current_sum)

        max_suffix_sum = 0
        current_sum = 0
        for x in reversed(arr):
            current_sum += x
            max_suffix_sum = max(max_suffix_sum, current_sum)

        ans = max_single_arr_sum
        
        max_spanning_two_blocks_sum = max_prefix_sum + max_suffix_sum

        if total_sum > 0:
            ans = max(ans, max_spanning_two_blocks_sum + (k - 2) * total_sum)
        else:
            ans = max(ans, max_spanning_two_blocks_sum)
        
        return ans % MOD