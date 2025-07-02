class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        duplicates = []
        for i in range(len(nums)):
            num = abs(nums[i])
            
            # The index corresponding to this number is num - 1.
            # If the value at nums[num - 1] is positive, it means we are seeing
            # 'num' for the first time. Mark it as seen by negating the value.
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
            # If the value at nums[num - 1] is negative, it means we have
            # already seen 'num' before. Since each number appears at most twice,
            # this 'num' must be a duplicate.
            else:
                duplicates.append(num)
        
        return duplicates