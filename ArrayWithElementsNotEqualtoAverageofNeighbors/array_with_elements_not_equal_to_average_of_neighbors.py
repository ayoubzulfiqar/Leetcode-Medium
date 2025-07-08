class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        result = []
        left = 0
        right = n - 1

        while left <= right:
            result.append(nums[left])
            left += 1
            if left <= right:
                result.append(nums[right])
                right -= 1
        
        return result