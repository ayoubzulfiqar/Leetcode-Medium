class Solution:
    def makeArrayNonDecreasing(self, nums: list[int]) -> int:
        n = len(nums)
        
        ans = 1
        current_max_val = nums[n - 1]
        
        for i in range(n - 2, -1, -1):
            if nums[i] <= current_max_val:
                ans += 1
                current_max_val = nums[i]
            else:
                current_max_val = nums[i]
                
        return ans