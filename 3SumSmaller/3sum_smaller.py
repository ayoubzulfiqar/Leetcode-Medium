class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        count = 0

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < target:
                    # If nums[i] + nums[left] + nums[right] < target,
                    # then any triplet (nums[i], nums[left], nums[k]) where left < k <= right
                    # will also have a sum less than target, because nums[k] <= nums[right].
                    # There are (right - left) such values for k.
                    count += (right - left)
                    left += 1  # Move left pointer to find new combinations
                else:
                    # The current sum is too large or equal to target, so we need to decrease it.
                    # This is done by moving the right pointer to a smaller value.
                    right -= 1

        return count