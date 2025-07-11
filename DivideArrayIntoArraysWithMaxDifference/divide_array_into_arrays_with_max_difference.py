import collections

class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        
        n = len(nums)
        result = []
        
        for i in range(0, n, 3):
            # Check if the difference between the largest and smallest element in the current triplet is <= k
            if nums[i+2] - nums[i] > k:
                return [] # Impossible to satisfy the condition
            
            result.append([nums[i], nums[i+1], nums[i+2]])
            
        return result