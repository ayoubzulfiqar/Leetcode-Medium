class Solution:
    def sumOfBeauties(self, nums: list[int]) -> int:
        n = len(nums)
        total_beauty = 0

        left_max = [0] * n
        max_so_far = nums[0]
        for i in range(1, n):
            left_max[i] = max_so_far
            max_so_far = max(max_so_far, nums[i])

        right_min = [0] * n
        min_so_far = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min_so_far
            min_so_far = min(min_so_far, nums[i])

        for i in range(1, n - 1):
            num_i = nums[i]
            
            if left_max[i] < num_i < right_min[i]:
                total_beauty += 2
            elif nums[i-1] < num_i < nums[i+1]:
                total_beauty += 1
            
        return total_beauty