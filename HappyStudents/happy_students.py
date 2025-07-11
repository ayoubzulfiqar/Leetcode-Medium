class Solution:
    def happyStudents(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()

        ways = 0

        if nums[0] > 0:
            ways += 1

        for k in range(1, n):
            if nums[k-1] < k and nums[k] > k:
                ways += 1

        if n > nums[n-1]:
            ways += 1
            
        return ways