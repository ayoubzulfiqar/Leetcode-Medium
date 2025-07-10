class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        nums.sort()
        
        greatness = 0
        i = 0
        j = 0
        
        while j < len(nums):
            if nums[j] > nums[i]:
                greatness += 1
                i += 1
                j += 1
            else:
                j += 1
                
        return greatness