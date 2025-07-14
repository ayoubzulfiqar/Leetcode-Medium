class Solution:
    def maximumDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        
        distinct_count = 0
        last_val = -float('inf') 
        
        for num in nums:
            if num - k > last_val:
                distinct_count += 1
                last_val = num - k
            elif last_val + 1 <= num + k:
                distinct_count += 1
                last_val = last_val + 1
            
        return distinct_count