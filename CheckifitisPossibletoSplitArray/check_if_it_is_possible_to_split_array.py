from typing import List

class Solution:
    def possibleToSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        
        if n == 1:
            return True

        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i+1] = prefix_sums[i] + nums[i]

        def get_sum(start, end):
            return prefix_sums[end+1] - prefix_sums[start]

        memo = {}

        def solve(left, right):
            if left == right:
                return True

            if (left, right) in memo:
                return memo[(left, right)]

            result = False
            for k in range(left, right):
                len_left = k - left + 1
                len_right = right - (k + 1) + 1

                sum_left = get_sum(left, k)
                sum_right = get_sum(k + 1, right)

                is_left_good = (len_left == 1) or (sum_left >= m)
                is_right_good = (len_right == 1) or (sum_right >= m)

                if is_left_good and is_right_good:
                    if solve(left, k) and solve(k + 1, right):
                        result = True
                        break
            
            memo[(left, right)] = result
            return result

        return solve(0, n - 1)