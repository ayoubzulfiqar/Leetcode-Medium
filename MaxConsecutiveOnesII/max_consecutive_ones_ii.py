class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left = 0
        zeros_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1

            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len