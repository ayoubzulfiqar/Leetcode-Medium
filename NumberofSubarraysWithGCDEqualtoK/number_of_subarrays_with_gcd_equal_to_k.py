import math

class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] % k != 0:
                continue

            current_gcd = 0

            for j in range(i, n):
                if nums[j] % k != 0:
                    break

                if j == i:
                    current_gcd = nums[j]
                else:
                    current_gcd = math.gcd(current_gcd, nums[j])

                if current_gcd == k:
                    count += 1
                elif current_gcd < k:
                    break
        return count