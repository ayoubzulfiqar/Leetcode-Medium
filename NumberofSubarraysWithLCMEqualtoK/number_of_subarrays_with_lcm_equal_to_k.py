import math

class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            current_lcm = 1
            for j in range(i, n):
                num = nums[j]

                if k % num != 0:
                    break

                current_lcm = (current_lcm * num) // math.gcd(current_lcm, num)

                if current_lcm > k:
                    break

                if current_lcm == k:
                    count += 1

        return count