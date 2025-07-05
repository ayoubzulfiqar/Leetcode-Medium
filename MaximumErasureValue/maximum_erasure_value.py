class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        max_sum = 0
        seen = set()

        for right in range(len(nums)):
            num = nums[right]
            while num in seen:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            
            current_sum += num
            seen.add(num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum