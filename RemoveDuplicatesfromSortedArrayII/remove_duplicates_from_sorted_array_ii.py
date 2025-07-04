class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(len(nums)):
            if i < 2 or nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        
        return i