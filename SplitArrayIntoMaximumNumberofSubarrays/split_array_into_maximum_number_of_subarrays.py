```python
class Solution:
    def maxSubarrays(self, nums: list[int]) -> int:
        total_and = nums[0]
        for i in range(1, len(nums)):
            total_and &= nums[i]
        
        if total_and > 0:
            return 1
        
        count = 0
        current_and = -1 
        
        for num in nums:
            current_and &= num
            
            if current_and == 0:
                count += 1
                current_and = -1
                
        return count

```