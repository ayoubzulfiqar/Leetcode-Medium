class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        MOD = 10**9 + 7

        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i-1] * 2) % MOD

        count = 0
        left = 0
        right = n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + powers[right - left]) % MOD
                left += 1
            else:
                right -= 1
        
        return count