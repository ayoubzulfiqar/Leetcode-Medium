import math

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        count_ones = nums.count(1)
        if count_ones > 0:
            return n - count_ones

        min_ops_to_create_one = float('inf')

        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_ops_to_create_one = min(min_ops_to_create_one, j - i)
                    break

        if min_ops_to_create_one == float('inf'):
            return -1
        else:
            return min_ops_to_create_one + (n - 1)